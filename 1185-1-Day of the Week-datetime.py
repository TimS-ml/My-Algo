# https://leetcode-cn.com/problems/day-of-the-week/


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days = [
            "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
            "Sunday"
        ]
        from datetime import datetime
        return days[datetime(year, month, day).weekday()]
