class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # result=[]
        # li=[]
        # for i in range(len(nums)):
        #     if nums[i]!=val:
        #         result.append(nums[i])
        # a=len(result)
        # for i in range(0,len(result)):
        #     if nums[i]!=val:
        #         li.append(nums[i])
        # li.append()
        
        k = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
                
        return k        


            



        