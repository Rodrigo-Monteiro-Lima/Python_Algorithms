def study_schedule(permanence_period, target_time=None):
    if target_time is None:
        return None

    students = 0

    for period in permanence_period:
        if (
            type(period) != tuple
            or len(period) != 2
            or type(period[0]) != int
            or type(period[1]) != int
            or period[0] > period[1]
            or period[0] < 0
            or period[1] < 0
        ):
            return None
        if period[0] <= target_time <= period[1]:
            students += 1

    return students
