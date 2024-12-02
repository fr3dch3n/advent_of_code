.DEFAULT_GOAL:= help

PYTHON := poetry run python
PYTEST := poetry run pytest

# Variables for year and day (optional overrides for convenience)
YEAR ?= 2024
DAY ?= 1

.PHONY: pre-commit-install
pre-commit-install: ## Install pre-commit
	pre-commit install

.PHONY: pre-commit
pre-commit: pre-commit-install ## Run pre-commit
	pre-commit run --all-files

.PHONY: install
install: ## Install dependencies with Poetry
	pre-commit install
	poetry install

.PHONY: test
test: install ## Run all tests for all years
	$(PYTEST) -n auto tests/

.PHONY: test-watch
test-watch: install ## Watch tests
	poetry run ptw

.PHONY: test-year
test-year: install ## Run all tests for a specific year
	$(PYTEST) tests/year_$(YEAR)

.PHONY: test-year-day
test-year-day: install ## Run tests for a specific day within a specific year
	$(PYTEST) tests/year_$(YEAR)/test_day_$(DAY).py

.PHONY: update
update: ## Update poetry deps
	poetry update

.PHONY: clean
clean: ## Clean up python cache
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

.PHONY: help
help: ## Show help message
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m\033[0m\n"} /^[$$()% a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)
