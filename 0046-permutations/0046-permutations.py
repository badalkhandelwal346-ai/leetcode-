class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
       arr=[]
       
       def f(i):
        if i==len(nums):
            arr.append(nums[:])
            return
        for j in range(i,len(nums)):
            nums[j],nums[i]=nums[i],nums[j]
            f(i+1)
            nums[j],nums[i]=nums[i],nums[j]
            
            

       f(0) 
       return arr
        


        
        