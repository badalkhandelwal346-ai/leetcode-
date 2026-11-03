class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        a=max(nums)
        total=0
        for i in range(len(nums)):
            total+=abs(nums[i]-a)
        return total    
        