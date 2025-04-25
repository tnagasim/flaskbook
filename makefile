format:
	isort .
	black .

lint:
	ruff check .
	flake8 .

fix:
	ruff check . --fix

check:
	black --check .
	ruff check . --diff
