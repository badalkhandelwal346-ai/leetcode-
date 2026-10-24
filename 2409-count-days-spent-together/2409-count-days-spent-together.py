class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        a = max(arriveAlice, arriveBob)
        b = min(leaveAlice, leaveBob)
        
        # If the start of overlap comes after the end, they don't overlap
        if a > b:
            return 0
        
        a = list(a)
        b = list(b)
        
        # 1. Join list characters before converting to int: "".join(...)
        # 2. Use sum(arr[:...]) for preceding months instead of multiplying
        month_days_1 = sum(arr[:int("".join(a[0:2])) - 1])
        days_1 = int("".join(a[3:5]))
        
        month_days_2 = sum(arr[:int("".join(b[0:2])) - 1])
        days_2 = int("".join(b[3:5]))  # Fixed: read from 'b', not 'a'
        
        # +1 because the date range is inclusive (e.g., same day = 1 day)
        return (month_days_2 + days_2) - (month_days_1 + days_1) + 1
