class Solution:
    def maxDistance(self, moves: str) -> int:
        y=0
        x=0
        count=0
        for i in moves:
            if i == "U":
                y+=1
            elif i == "R":
                x+=1
            elif i == "D":
                y-=1
            elif i == "L":
                x-=1
            else:
                count+=1
        return abs(x)+abs(y)+count        
               
                                

        