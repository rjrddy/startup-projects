ROOT := $(abspath ../..)
PY := $(ROOT)/.venv/bin/python
export PYTHONPATH := $(CURDIR)/src
export MPLBACKEND := Agg
export MPLCONFIGDIR := /tmp/outreach-matplotlib
.PHONY: setup test bench demo lint
setup:
	python3 -m venv $(ROOT)/.venv
	$(PY) -m pip install -r $(ROOT)/requirements.txt
lint:
	$(PY) -m ruff check src tests
	$(PY) -m ruff format --check src tests
test:
	$(PY) -m pytest -q
bench:
	@mkdir -p evidence
	$(PY) src/$(ENTRY).py > evidence/bench.json
	@cat evidence/bench.json
demo: bench
