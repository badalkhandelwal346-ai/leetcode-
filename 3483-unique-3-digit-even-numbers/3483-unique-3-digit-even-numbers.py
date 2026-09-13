class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        vis=[False]*1000
        ans=0
        for i in range(len(digits)):
            if digits[i]==0:
                continue
            for j in range(len(digits)):
                if [j]==[i]:
                    continue
                for k in range(len(digits)):
                    if [k]==[j] or [k]==[i] or digits[k]%2!=0:
                        continue
                    x=digits[i]*100 + digits[j]*10 + digits[k]
                    if not vis[x]:
                        vis[x]=True
                        ans+=1
        return ans                







        