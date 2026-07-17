class Solution:
    def lexSmallest(self, s: str) -> str:
        n=len(s)
        arr=[]
        for i in range(1,len(s)+1):
            a=s[0:i+1]
            a=a[::-1]
            b=s[i+1:len(s)]

            arr.append(a+b)
            arr.append(s[:n-i] + s[n-i:][::-1])
            
        return min(arr)    

            