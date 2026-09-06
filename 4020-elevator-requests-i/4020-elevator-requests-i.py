class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        a=0
        count=0
        for i in range(len(requests)):
            count+=abs(requests[i]-a)
            a=requests[i]
        return count    

            