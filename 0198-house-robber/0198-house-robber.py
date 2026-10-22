class Solution:
    def rob(self, nums: list[int]) -> int:
        dp=[-1]*len(nums)
        def f(i):
            if i>=len(nums):
                return 0
            if dp[i]!=-1:
                return dp[i]    
            a=nums[i]+f(i+2)
            b=f(i+1)
            dp[i]=max(a,b)
            return dp[i]
        return f(0)

