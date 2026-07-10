class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        middle=nums[len(nums)//2]
        count=0
        for i in range(len(nums)):
            if nums[i]==middle:
                count+=1
        if count>1:
            return False
        else:
            return True            
