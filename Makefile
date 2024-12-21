install:
	uv sync

build:
	uv build

package-install:
	uv tool install dist/*.whl

package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

gendiff:
	uv run gendiff

lint:
	uv run ruff check .

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml

check: test lint

.PHONY: install test lint selfcheck check build