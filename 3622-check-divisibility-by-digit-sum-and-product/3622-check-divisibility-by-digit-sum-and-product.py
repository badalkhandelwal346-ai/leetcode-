class Solution:
    def checkDivisibility(self, n: int) -> bool:
        c=n
        n=str(n)
        n=list(n)
        a=0
        b=1
        for i in range(len(n)):
            a+=int(n[i])
            b*=int(n[i])
        if c%(a+b)==0:
            return True
        else:
            return False                  
