.PHONY: setup
setup:
	@pipenv install -d

.PHONY: shell
shell:
	@pipenv shell

.PHONY: mypy
mypy:
	@mypy --strict  -p planner
