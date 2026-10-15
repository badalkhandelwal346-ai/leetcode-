class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)):
            curr=[]
            curr.append(nums[i])
            ans+=len(set(curr))**2
            for j in range(i+1,len(nums)):
                curr.append(nums[j])
                ans+=len(set(curr))**2
        return ans       

                
                
                         

        