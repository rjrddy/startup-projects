from harness import evaluate, gate


def test_identical_seed_identical_scores():
    assert evaluate(8, episodes=4) == evaluate(8, episodes=4)


def test_bad_policy_fails_and_good_passes():
    assert not gate(evaluate(0))
    assert gate(evaluate(8))


def test_scenarios_change_with_seed():
    assert evaluate(0, 42)["errors"] != evaluate(0, 43)["errors"]
