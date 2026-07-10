class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        maxi=nums[0]
        n=len(nums)
        ans=float("-inf")
        for i in range(k,n):
            maxi=max(maxi,nums[i-k])
            ans=max(maxi+nums[i],ans)
        return ans 



        