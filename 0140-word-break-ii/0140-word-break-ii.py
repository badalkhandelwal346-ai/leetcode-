class Solution:
    def wordBreak(self,s: str, wordDict: List[str]) -> List[str]:
        curr=[]
        ans=[]
        def f(i):
            if i==len(s):
                ans.append(" ".join(curr))
                return 
            for j in range(i,len(s)):
                if s[i:j+1] in wordDict:
                    curr.append(s[i:j+1])
                    f(j+1)
                    curr.pop()
        f(0) 
        return ans




           