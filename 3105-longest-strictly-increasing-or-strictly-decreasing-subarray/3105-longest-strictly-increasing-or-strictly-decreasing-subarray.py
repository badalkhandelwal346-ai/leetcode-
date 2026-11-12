class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        count=1
        maxi=0
        total=1
        maxi_1=0

        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                count+=1
            else:
                maxi=max(count,maxi)
                count=1
        a=max(maxi,count) 
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                total+=1
            else:
                maxi_1=max(total,maxi_1)
                total=1
        b=max(maxi_1,total)
        return max(a,b)        
                 

            
            