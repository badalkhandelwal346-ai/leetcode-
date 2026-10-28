class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max=1
        for i in range(len(nums)//2):
            if nums[i]+nums[len(nums)-(i+1)]>max:
                max=nums[i]+nums[len(nums)-(i+1)]
        return max        

            