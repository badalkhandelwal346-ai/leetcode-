class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums.sort()
        a=k
        for i in range(len(nums)):
            if nums[i]==k:
                k+=a
        return k        

                  
        
              
