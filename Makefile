.PHONY: lint lint-fix format typecheck all

lint:
	ruff check .

lint-fix:
	ruff check . --fix

format:
	black .

typecheck:
	mypy .

all: lint format typecheck