from validator import corpus, decide


def test_all_generated_invalid_actions_rejected():
    assert all(not decide(raw)["accepted"] for raw in corpus())


def test_finite_and_strict():
    for x in [float("nan"), float("inf"), True, "0.2"]:
        assert not decide({"kind": "move", "x": x, "y": 0.0, "z": 0.5, "steps": 1})["accepted"]


def test_replay_including_rejections():
    for raw in corpus(count=20) + [{"kind": "move", "x": 0.2, "y": 0.3, "z": 0.4, "steps": 10}]:
        assert decide(raw) == decide(raw)


def test_simulator_endpoint():
    result = decide({"kind": "move", "x": 0.2, "y": 0.3, "z": 0.4, "steps": 10})
    assert result["position"] == [0.2, 0.3, 0.4]
