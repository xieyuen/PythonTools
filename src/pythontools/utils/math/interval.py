from __future__ import annotations
from numbers import Real


class Interval:
    def __init__(self, start: Real, end: Real, closed: tuple[bool, bool] = (True, True)):
        self.interval: tuple[Real, Real] = (start, end)
        self.closed = closed
        self.__check_interval_valid()

    def __check_interval_valid(self):
        start, end = self.interval
        if start > end:
            raise ValueError(f"Invalid interval: {list(self.interval)}")
        if start == end:
            left, right = self.closed
            self.is_empty = not (left and right)
        else:
            self.is_empty = False

    # self == other
    def __eq__(self, other: "Interval") -> bool:
        if self.is_empty ^ other.is_empty:
            return False
        if self.is_empty:
            return True
        return self.interval == other.interval and self.closed == other.closed

    # self < other
    def __lt__(self, other: "Interval"):
        if self.is_empty:
            return True
        if other.is_empty:
            return False

        if self.interval == other.interval:
            return (
                    not self.closed[0] and other.closed[0]
            ) or (
                    not self.closed[1] and other.closed[1]
            )
        return (
                self.interval[0] >= other.interval[0]
        ) and (
                self.interval[1] <= other.interval[1]
        )

    def __le__(self, other: "Interval"):
        return self < other or self == other

    def __gt__(self, other: "Interval"):
        return not self <= other

    def __ge__(self, other: "Interval"):
        return not self < other

    def __contains__(self, item: "Interval" | Real) -> bool:
        if isinstance(item, Interval):
            return self >= item

        if self.is_empty:
            return False
        left, right = self.closed
        start, end = self.interval
        if (item == start and left) or (item == end and right):
            return True
        return start < item < end

    def __repr__(self) -> str:
        left, right = self.closed
        start, end = self.interval
        return (
                f"{'[' if left else '('}" +
                f"{start}, {end}" +
                f"{']' if right else ')'}"
        )
