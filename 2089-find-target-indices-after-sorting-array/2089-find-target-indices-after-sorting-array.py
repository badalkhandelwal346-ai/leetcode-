class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        curr=[]
        for i in range(len(nums)):
            if nums[i]==target:
                curr.append(i)
        return curr        