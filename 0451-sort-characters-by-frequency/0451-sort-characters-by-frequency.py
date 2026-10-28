class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        for i in range(len(s)):
            if s[i] in freq:
                freq[s[i]]+=1
            else:
                freq[s[i]]=1
        # return freq  
        freq=(sorted(freq.items(), key=lambda x: x[1], reverse=True))
        # return freq
        return ''.join(ch * count for ch, count in freq)
