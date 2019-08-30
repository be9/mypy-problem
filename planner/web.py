from planner.scheduling import RandyScheduleBuilder, ScheduleBuilder, book_campaign, cancel_campaign, reserve_campaign


def schedule_builder_maker() -> ScheduleBuilder:
    return RandyScheduleBuilder()


def foo() -> None:
    book_campaign()
    reserve_campaign()
    cancel_campaign()


foo()
