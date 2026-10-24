class Solution:
    def rob(self, nums: list[int]) -> int:
        dp=[-1]*(len(nums))
        dp_2=[-1]*(len(nums))
        if len(nums)==1:
            return nums[0]

        


        def f(i):
            if i>=len(nums):
                return 0
            if dp[i]!=-1:
                return dp[i]    
            a=nums[i]+f(i+2)
            b=f(i+1)
            dp[i]=max(a,b)
            return dp[i]
        a=f(1)
        nums_2=nums[0:len(nums)-1]
        def F(i):
            if i>=len(nums_2):
                return 0
            if dp_2[i]!=-1:
                return dp_2[i]    
            a=nums_2[i]+F(i+2)
            b=F(i+1)
            dp_2[i]=max(a,b)
            return dp_2[i]
        b=F(0) 
        return max(a,b)   


        