PYTHON ?= python3

.PHONY: lint test smoke validate run

lint:
	$(PYTHON) scripts/lint.py

validate:
	$(PYTHON) -m luna validate

test:
	$(PYTHON) -m unittest discover -s tests -p 'test_*.py'

smoke:
	$(PYTHON) scripts/smoke_test.py

run:
	$(PYTHON) -m luna run --brief examples/content_brief.json --memory examples/memory.json --analytics examples/analytics_feedback.json
