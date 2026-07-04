class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        freq={}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
        arr=[]
        for key,value in freq.items():
            if freq[key]>=k:
                arr.extend([key] * k)
            else:
                arr.extend([key] * value)
        return arr                      
        
        