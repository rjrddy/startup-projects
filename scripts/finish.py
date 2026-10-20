"""Render documented measurements from an actual benchmark artifact."""
import json
import sys
from pathlib import Path

p = Path(sys.argv[1])
meta = json.loads((p / "project.json").read_text())
metrics = json.loads((p / "evidence/bench.json").read_text())
lines = [f'{label}: {metrics[key]}{suffix}' for label, key, suffix in meta['results']]
readme = f'''1. {meta["problem"]}

2. Result:
{chr(10).join("   " + line + "  " for line in lines)}

   Measured by `make bench`; raw [results](evidence/bench.json), [checks](evidence/checks.log), and [environment](evidence/environment.json).

3. Architecture:
```mermaid
flowchart LR
    {meta["diagram"]}
```

4. Run it (from this folder):
```sh
make setup
make lint test bench
{meta.get("command", "make demo")}
```

5. Decisions and limits: {meta["limits"]}

6. Next: {meta["next"]}
'''
(p / 'README.md').write_text(readme)
portfolio = Path('PORTFOLIO.md')
rows = portfolio.read_text().splitlines()
rows = [r for r in rows if not r.startswith(f'| {meta["id"]} |')]
rows.append(f'| {meta["id"]} | {meta["name"]} | {lines[0]} | [{p.name}]({p}) | {meta["status"]} |')
portfolio.write_text('\n'.join(rows) + '\n')
print('\n'.join(lines))
