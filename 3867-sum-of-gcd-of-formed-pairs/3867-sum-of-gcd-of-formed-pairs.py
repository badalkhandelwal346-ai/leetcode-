from math import gcd
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        total=0
        maxi=1
        prefixGcd=[]
        arr=[]
        for i in range(len(nums)):
            
            maxi=max(maxi,nums[i])
            prefixGcd.append(gcd(nums[i],maxi))
        prefixGcd.sort()
        a=0
        b=len(prefixGcd)-1
        for i in range(len(prefixGcd)//2):
            total+=gcd(prefixGcd[i],prefixGcd[b-i])
        return total   


