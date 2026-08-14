class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        best=0
        for i in range(len(s)):
            freq={}
            count=0
            for j in range(i,len(s)):
                freq[s[j]] = freq.get(s[j], 0)
                if freq[s[j]]<2:
                    freq[s[j]]+=1
                    count+=1
                else:
                    
                    break
            best=max(best,count)        
        return best            


