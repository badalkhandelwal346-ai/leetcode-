class Solution:
    def reverse(self, x: int) -> int:
        x=str(x)
        if x=="0":
            return 0
        x=list(x)
        
        while x and x[-1]=="0":
            x=x[0:len(x)-1]
        if x[0]=="-":
            x.reverse()
            x.pop()
            a="".join(x)
            a=int(a)
            if a>2147483647 or a<-2147483648:
                return 0
            else:
                return -a    
        else:
            x.reverse()
            a="".join(x)
            a=int(a)
            if a>2147483647 or a<-2147483648:
                return 0
            else:
                return a  
            



               

        