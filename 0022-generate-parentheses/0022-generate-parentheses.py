class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        arr=[]
        def f(i,ope,close):
            if i==2*n:
                arr.append("".join(temp))
                return
            if ope<n:
                temp.append('(')
                f(i+1,ope+1,close)
                temp.pop()
            if ope>close:
                temp.append(')') 
                f(i+1,ope,close+1)
                temp.pop()
        temp=[]
        f(0,0,0)
        return arr           

        
        
        
        