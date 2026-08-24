class Solution:
    def isPalindromic(self, s: str) -> bool:
        a=""
        for ch in s:
            ascii_value=ord(ch)
            binary_value=bin(ascii_value)[2:]
            binary_value = binary_value.zfill(8)
            a+=binary_value
        for i in range(len(a)//2+1):
            if a[i]!=a[len(a)-i-1]:
                return False
        return True 
                
                




        