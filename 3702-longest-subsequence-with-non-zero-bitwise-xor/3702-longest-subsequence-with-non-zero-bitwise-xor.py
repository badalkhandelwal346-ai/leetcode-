class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        if all(x == 0 for x in nums):
            return 0
        xor=0
        for  a in nums:
            xor^=a
        if xor==0:
            return len(nums)-1
        else:
            return len(nums)        
        