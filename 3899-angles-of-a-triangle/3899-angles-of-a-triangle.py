import math
class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        arr=[]
        a=sides[0]
        b=sides[1]
        c=sides[2]
        if a+b<=c or  b+c<=a or  a+c<=b:
            return []
        arr.append(math.degrees(math.acos((c**2+b**2-a**2)/(2*c*b))))
        arr.append(math.degrees(math.acos((a**2+c**2-b**2)/(2*a*c))))
        arr.append(math.degrees(math.acos((a**2+b**2-c**2)/(2*a*b))))
        if math.isclose(sum(arr),180,abs_tol=1e-6):
            arr.sort()
            return arr
        return []    
       
        
            
        