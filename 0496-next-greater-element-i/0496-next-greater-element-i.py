class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        result=[]
        outcome=[]
        for i in range(len(nums2)-1,-1,-1):
            while stack and nums2[i]>=stack[-1]:
                stack.pop()
            if stack:
                result.append(stack[-1])
                stack.append(nums2[i])
            else:
                result.append(-1)
                stack.append(nums2[i])
        result=result[::-1]
        j=0
        while j<len(nums1):
            for i in range(len(nums2)):
                if nums1[j]==nums2[i]:
                    outcome.append(result[i])
                    j+=1
                    break
        return outcome            



            

            
            
       
                    
                    