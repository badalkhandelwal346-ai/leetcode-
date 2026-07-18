class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
       count=0
       total=0
       a=""
       for i in range(len(s)):
        if s[i]==y:
            count+=1
        elif s[i]==x:
            total+=1
        else:
            a=a+s[i]
       return y*count+x*total+a        
                
                    
        