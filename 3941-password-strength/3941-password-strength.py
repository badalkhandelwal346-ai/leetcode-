class Solution:
    def passwordStrength(self, password: str) -> int:
       
        password = "".join(set(password))
        count=0
        for i in range(len(password)):
            if 65<=ord(password[i])<=90:
                count+=2
            elif 97<=ord(password[i])<=122:
                count+=1
            elif password[i] in "!@#$":
                count+=5                
            
            else:
                count+=3
        return count                
        