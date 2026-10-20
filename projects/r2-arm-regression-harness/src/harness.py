"""Seeded MuJoCo single-joint arm scenarios and a policy regression gate."""

import argparse
import json
import random
from pathlib import Path

import mujoco

XML = """<mujoco><option timestep="0.01" gravity="0 0 0"/>
<worldbody><body><joint name="hinge" type="hinge" axis="0 0 1" damping="1"/>
<geom type="capsule" fromto="0 0 0 1 0 0" size="0.04" mass="1"/>
</body></worldbody><actuator><motor joint="hinge" ctrllimited="true" ctrlrange="-10 10"/>
</actuator></mujoco>"""


def evaluate(gain: float, seed: int = 42, episodes: int = 30) -> dict:
    model = mujoco.MjModel.from_xml_string(XML)
    rng = random.Random(seed)
    errors = []
    for _ in range(episodes):
        data = mujoco.MjData(model)
        target = rng.uniform(-1.0, 1.0)
        for _ in range(400):
            data.ctrl[0] = gain * (target - data.qpos[0]) - 2.0 * data.qvel[0]
            mujoco.mj_step(model, data)
        errors.append(abs(target - float(data.qpos[0])))
    return {
        "gain": gain,
        "seed": seed,
        "episodes": episodes,
        "successes": sum(e < 0.05 for e in errors),
        "errors": errors,
        "success_rate": sum(e < 0.05 for e in errors) / episodes,
    }


def gate(result: dict, minimum: float = 0.9) -> bool:
    return result["success_rate"] >= minimum


def benchmark() -> dict:
    results = {name: evaluate(gain) for name, gain in [("v1", 0.0), ("v2", 1.0), ("v3", 8.0)]}
    assert results["v3"] == evaluate(8.0)
    assert not gate(results["v1"])
    return {
        "policies": results,
        "policy_versions": len(results),
        "repeat_identical": True,
        "best_successes": results["v3"]["successes"],
        "episodes": results["v3"]["episodes"],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--gate", action="store_true")
    parser.add_argument("--gain", type=float)
    args = parser.parse_args()
    if args.gate:
        gain = (
            args.gain
            if args.gain is not None
            else json.loads(Path("policy.json").read_text())["gain"]
        )
        result = evaluate(gain)
        print(json.dumps(result, indent=2))
        print("PASS" if gate(result) else "FAIL: success rate below 0.9")
        raise SystemExit(0 if gate(result) else 1)
    print(json.dumps(benchmark(), indent=2))
