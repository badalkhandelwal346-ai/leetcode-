class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        result=[]
        arr=[]
        def f(i,st):
            if i==n:
                arr.append(st)
                return 
                
                   
            f(i+1,st+"0")
            f(i+1,st+'1')
        f(0,"")
        for s in arr:
            if "11" not in s:
                result.append(s)
        new=[]
       
        for i in range(len(result)):
            count=0
            for j in range(len(result[i])):
                if result[i][j]=="1":
                    count+=j
            if count<=k:
                new.append(result[i])
        return new                
            



            
            




        