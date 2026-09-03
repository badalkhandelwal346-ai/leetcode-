class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        ones=[]
        twoes=[]
        for i in range(len(nums)):
            if nums[i]==1:
                ones.append(i)
            if nums[i]==2:
                twoes.append(i)
        if len(ones)==0 or len(twoes)==0:
            return -1
        min=1000  
        for i in range(len(ones)):
            for j in range(len(twoes)):
                if abs(ones[i]-twoes[j])<min:
                    min=abs(ones[i]-twoes[j])
        return min            

