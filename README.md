# mypy-problem

A repo that illustrates the problem with mypy.

## Running mypy

```bash
pipenv install -d
pipenv shell
```

Then `mypy --strict  -p planner`.

## Expected behavior

There should be no errors/warnings from mypy, since the code is correct (can be verified by running `python -m planner.web`).

## Actual behavior

`mypy --strict  -p planner` (with mypy 0.720):

```
planner/web.py:1: error: Module 'planner.scheduling' has no attribute 'RandyScheduleBuilder'; maybe "ScheduleBuilder"?
planner/web.py:1: error: Module 'planner.scheduling' has no attribute 'ScheduleBuilder'; maybe "ScheduleBuilderMaker" or "RandyScheduleBuilder"?
planner/web.py:1: error: Module 'planner.scheduling' has no attribute 'book_campaign'
planner/web.py:1: error: Module 'planner.scheduling' has no attribute 'cancel_campaign'
planner/web.py:1: error: Module 'planner.scheduling' has no attribute 'reserve_campaign'
```
