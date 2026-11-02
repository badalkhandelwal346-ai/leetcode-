from math import floor,ceil
class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        a=nums[len(nums)//2]
        count=0
        # total=0
        for i in range(len(nums)):
            count+=min(floor(abs(nums[i]-a)),ceil(abs(nums[i]-a)))

            
        return count    