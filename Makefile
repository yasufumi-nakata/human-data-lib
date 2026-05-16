.PHONY: validate test stats

validate:
	PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m human_data_lib.cli validate

test:
	PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m unittest discover -s tests -p 'test_*.py'

stats:
	PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m human_data_lib.cli stats --facet domains
