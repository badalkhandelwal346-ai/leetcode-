class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        tokens.sort()
        i=0
        j=len(tokens)-1
        score=0
        maxi=0
        # if tokens[0]>power:
        #     return 0
        while i<=j:
            if power>=tokens[i]:
                power-=tokens[i]
                score+=1
                
                i+=1
            else:
                if score>=1:
                    power+=tokens[j]
                    score-=1
                j-=1
            maxi=max(maxi,score)
        return maxi