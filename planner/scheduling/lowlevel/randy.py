"""Dumb and greedy scheduler implementation."""
from dataclasses import dataclass

from planner.scheduling.lowlevel.base import ScheduleBuilder


class RandyScheduleBuilder(ScheduleBuilder):
    @dataclass(frozen=True)
    class Results(ScheduleBuilder.Results):
        """Extends ScheduleBuilder.Results with algorithm-specific results."""
        details: str

    def build(self) -> None:
        pass