class Solution:
    def countCommas(self, n: int) -> int:
        if 1<=n<=999:
            return 0
        if n==10**5:
            return 1+(99999-999)
        else:
            return n-999    

        