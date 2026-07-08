class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        count=0
        freq={}
        n=str(n)
        for i in range(len(n)):
            if n[i] in freq:
                freq[n[i]]+=1
            else:
                freq[n[i]]=1
        for key,value in freq.items():
            count+=int(key)*value
        return count    
