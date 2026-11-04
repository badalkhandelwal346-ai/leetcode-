class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        arr=[]
        for i in range(len(nums)-k,len(nums)):
            arr.append(nums[i])
        for i in range(len(nums)-k):
            arr.append(nums[i])
        nums[:]=arr     
        