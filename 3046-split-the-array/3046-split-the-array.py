class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        freq={}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
        for key,value in freq.items():
            if freq[key]>=3:
                return False
                
        else:
            return True                    
        
        
