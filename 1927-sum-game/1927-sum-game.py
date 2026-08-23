class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        diff = 0
        q_left = 0
        q_right = 0

        for i in range(half):
            if num[i] == '?':
                q_left += 1
            else:
                diff += int(num[i])

        for i in range(half, n):
            if num[i] == '?':
                q_right += 1
            else:
                diff -= int(num[i])

        # Odd number of '?' means Alice has an extra move
        if (q_left + q_right) % 2 == 1:
            return True

        # Bob can win only if the difference can be exactly balanced
        return diff != 9 * (q_right - q_left) // 2