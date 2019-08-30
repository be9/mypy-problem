"""
Make schedule for capacity and budget campaigns.
"""
from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class LowLevelSchedulingStats:
    """Low-level stats."""
    pass


def make_schedule() -> Sequence[LowLevelSchedulingStats]:
    return []