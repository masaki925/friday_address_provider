.PHONY: help

.DEFAULT_GOAL := help

ADDRESS = "Winterallee 3"

init: ## init
	poetry install

test: init ## run test
	poetry run pytest -v tests

run: ## run convertion (e.g. $ make run ADDRESS="Winterallee 3")
	poetry run python src/address_provider/main.py --address "$(ADDRESS)"

help: ## help lists
	@grep -E '^[a-zA-Z_0-9-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
