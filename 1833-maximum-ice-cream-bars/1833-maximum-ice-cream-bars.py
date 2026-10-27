class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs.sort()
        amount=0
        for i in range(len(costs)):
            if costs[i]<=coins:
               coins=coins-costs[i]
               amount+=1
            else:
                break   
        return amount    
