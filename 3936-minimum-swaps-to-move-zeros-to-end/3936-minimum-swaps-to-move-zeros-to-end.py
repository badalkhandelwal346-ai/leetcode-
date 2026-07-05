class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        count=0
        for i in range(len(nums)):
            if nums[i]==0:
                count+=1
        nums=nums[::-1]
        swaps=0
        i=0
        while count!=0:
            if nums[i]==0:
                count-=1
            else:
                swaps+=1
                count-=1
            i+=1 
        return swaps       

            

        