class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        a=nums
        a=a[::-1]
        nums.extend(a)
        return nums