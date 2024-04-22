DEV_PORT = 80


.PHONY: tests
tests:
	pytest
	

.PHONY: app-dev
app-dev:
	uvicorn src.app.app:app --factory --reload --host 0.0.0.0 --port ${DEV_PORT}
