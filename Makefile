PYTHON ?= python

.PHONY: test lint format check

test:
	$(PYTHON) -m pytest -q

lint:
	ruff check .

format:
	black .

check: lint test
