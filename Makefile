check:
	pylint todotxt
	pycodestyle todotxt
	mypy todotxt --ignore-missing-imports
docs:
	sphinx-build -b html ./source ./build
pytest:
	pytest --cov todotxt --cov-report term-missing