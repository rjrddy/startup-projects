"""Record command evidence and machine provenance without inventing results."""
import argparse
import json
import platform
import subprocess
import time
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("project")
args = parser.parse_args()
project = Path(args.project)
started = time.time()
run = subprocess.run(["make", "lint", "test", "bench"], cwd=project, capture_output=True, text=True)
folder = project / "evidence"
folder.mkdir(exist_ok=True)
(folder / "checks.log").write_text(run.stdout + run.stderr)
(folder / "environment.json").write_text(json.dumps({"platform": platform.platform(),
    "python": platform.python_version(), "command": "make lint test bench", "exit_code": run.returncode,
    "elapsed_seconds": time.time() - started}, indent=2))
print(run.stdout + run.stderr)
raise SystemExit(run.returncode)
