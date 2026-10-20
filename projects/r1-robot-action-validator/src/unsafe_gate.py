"""Deliberately unsafe baseline: regression gate must reject this policy."""

from validator import corpus


def unsafe_accept(_: object) -> bool:
    return True


if __name__ == "__main__":
    accepted_invalid = sum(unsafe_accept(raw) for raw in corpus())
    print(f"FAIL: unsafe baseline accepted {accepted_invalid} invalid actions")
    raise SystemExit(1 if accepted_invalid else 0)
