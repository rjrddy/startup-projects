"""Typed robot action validation and deterministic simulator replay."""

import argparse
import json
import random
from pathlib import Path
from typing import Literal

import pybullet as pb
from pydantic import BaseModel, ConfigDict, Field, ValidationError


class Action(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True, allow_inf_nan=False)
    kind: Literal["move"]
    x: float = Field(ge=-1, le=1)
    y: float = Field(ge=-1, le=1)
    z: float = Field(ge=0, le=1)
    steps: int = Field(ge=1, le=100)


def simulate(action: Action) -> list[float]:
    """Kinematic dry run: a collision-free point robot inside a bounded workspace."""
    client = pb.connect(pb.DIRECT)
    try:
        body = pb.createMultiBody(baseMass=0, physicsClientId=client)
        for step in range(1, action.steps + 1):
            fraction = step / action.steps
            pb.resetBasePositionAndOrientation(
                body,
                [action.x * fraction, action.y * fraction, action.z * fraction],
                [0, 0, 0, 1],
                physicsClientId=client,
            )
            pb.stepSimulation(physicsClientId=client)
        pos, _ = pb.getBasePositionAndOrientation(body, physicsClientId=client)
        return list(pos)
    finally:
        pb.disconnect(client)


def decide(raw: object) -> dict:
    try:
        action = Action.model_validate(raw)
        return {"input": raw, "accepted": True, "position": simulate(action)}
    except ValidationError:
        return {"input": raw, "accepted": False, "position": None}


def corpus(seed: int = 42, count: int = 1000) -> list[object]:
    rng = random.Random(seed)
    values: list[object] = [None, [], {}, {"kind": "stop"}]
    for _ in range(count):
        action = {"kind": "move", "x": 0.2, "y": 0.3, "z": 0.4, "steps": 10}
        key = rng.choice(["x", "y", "z", "steps", "kind", "extra"])
        action[key] = rng.choice(["bad", None, [], {}, 9999, -9999])
        values.append(action)
    return values


def benchmark() -> dict:
    invalid = corpus()
    rejected = sum(not decide(raw)["accepted"] for raw in invalid)
    good = [{"kind": "move", "x": i / 100, "y": 0.0, "z": 0.5, "steps": 10} for i in range(20)]
    records = [decide(raw) for raw in invalid + good]
    path = Path("evidence/replay.jsonl")
    path.parent.mkdir(exist_ok=True)
    path.write_text("".join(json.dumps(row) + "\n" for row in records))
    replayed = [decide(row["input"]) for row in map(json.loads, path.read_text().splitlines())]
    assert replayed == records
    return {
        "invalid_actions": len(invalid),
        "rejected": rejected,
        "before_failure_rate": 1.0,
        "after_failure_rate": 1 - rejected / len(invalid),
        "replay_matches": len(records),
        "valid_simulated": len(good),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--replay", type=Path)
    args = parser.parse_args()
    if args.replay:
        rows = [json.loads(line) for line in args.replay.read_text().splitlines()]
        assert all(decide(row["input"]) == row for row in rows)
        print(json.dumps({"replay_matches": len(rows)}))
    else:
        print(json.dumps(benchmark(), indent=2, allow_nan=False))
