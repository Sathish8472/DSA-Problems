class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        available_days = 0
        current_last = 1

        for start, end in meetings:

            if start > current_last:
                available_days += start - current_last

            current_last = max(current_last, end + 1)

        if current_last <= days:
            available_days += days - current_last + 1

        return available_days



    def countDays_1(self, days: int, meetings: List[List[int]]) -> int:
        available_days = [True] * (days + 1)

        for meeting in meetings:
            start = meeting[0]
            end = meeting[1]

            while start <= end:
                available_days[start] = False
                start += 1

        available_days[0] = False

        return sum(1 for day in available_days if day == True)
