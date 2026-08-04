class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr=[]
        for i in range(nums[0],nums[-1]+1):
            if i in nums:
                continue
            else:
                arr.append(i)    
        return arr

