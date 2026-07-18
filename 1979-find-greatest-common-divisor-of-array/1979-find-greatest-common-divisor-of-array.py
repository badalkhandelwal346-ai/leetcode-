class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a=max(nums)
        b=min(nums)
        for i in range(b+1,0,-1):
            if a%i==0 and b%i==0:
                return i