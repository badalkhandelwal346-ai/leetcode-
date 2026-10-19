class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        # if len(nums)==1:
        #     return 0
        i=0
       
        while i<len(nums):
            if sum(nums[:i])==sum(nums[i+1:]):
                return i
            else:
                i+=1
        return -1        
                





        