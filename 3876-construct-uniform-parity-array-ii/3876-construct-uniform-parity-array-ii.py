class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd=[]
        even=[]
        for i in range(len(nums1)):
            if nums1[i]%2==0:
                even.append(nums1[i])
            else:
                odd.append(nums1[i])
        j=0
        k=0
        if len(even)==0 or len(odd)==0:
            return True      
        while j<len(even) and k<len(odd):
            if even[j]-odd[k]>=1:
                j+=1
            else:
                k+=1
        if j==len(even):
            return True
        if k==len(odd):
            return False                
            
