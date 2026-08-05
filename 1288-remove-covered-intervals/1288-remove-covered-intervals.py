class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        arr=[]
        
        for i in range(len(intervals)):
            covered=False
            for j in range(len(intervals)):
                if i==j:
                    continue
                if intervals[j][0]<=intervals[i][0] and intervals[i][1]<=intervals[j][1]:
                    covered=True
                    break
                else:
                    continue    
            if not covered:
                arr.append(i)
            
                    
        return len(arr)          
