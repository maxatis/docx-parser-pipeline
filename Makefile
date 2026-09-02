.PHONY: format lint check

format:
	ruff check --fix .
	ruff format .
lint:
	ruff check .
	ruff format --check .
	mypy src/ main.py
	deptry .

check: format lint
