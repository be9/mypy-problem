"""Base schedule builder interface."""
import abc
from dataclasses import dataclass
from typing import Callable


class ScheduleBuilder(abc.ABC):
    """Base class for schedule builders."""

    @dataclass(frozen=True)
    class Results:
        pass

    @abc.abstractmethod
    def build(self) -> None:
        pass


ScheduleBuilderMaker = Callable[[], ScheduleBuilder]
