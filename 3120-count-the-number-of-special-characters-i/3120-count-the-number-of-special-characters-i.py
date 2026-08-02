class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        a=""
        b=""
        count=0
        word=set(word)
        word=str(word)
        for i in range(len(word)):
            if word[i].islower():
                a+=word[i]
            else:
                b+=word[i]
        for i in range(len(a)):
            if a[i].upper() in b:
                count+=1
        return count        
                
            


        