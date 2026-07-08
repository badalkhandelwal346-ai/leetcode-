class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        count=0
        total=0
        for i in range(len(nums)):
            
            count+=nums[i]
            if count==0:
                total+=1
        return total            


        