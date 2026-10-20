"""Save an expected failing subprocess, and fail if it unexpectedly passes."""
import subprocess
import sys
from pathlib import Path

folder, *command = sys.argv[1:]
p = Path(folder)
result = subprocess.run(command, cwd=p, text=True, capture_output=True)
(p / 'evidence').mkdir(exist_ok=True)
(p / 'evidence/gate-failure.log').write_text('$ ' + ' '.join(command) + '\n' + result.stdout + result.stderr + f'\nexit_code={result.returncode}\n')
print(result.stdout + result.stderr)
assert result.returncode == 1, f'Expected deliberate gate failure, got {result.returncode}'
