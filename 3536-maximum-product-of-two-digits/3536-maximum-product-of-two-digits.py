class Solution:
    def maxProduct(self, n: int) -> int:
        n=str(n)
        n=list(n)
        n.sort()
        return int(n[-1])*int(n[-2])
        