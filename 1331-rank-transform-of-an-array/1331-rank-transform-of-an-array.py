class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        freq={}
        a=arr[:]
        a.sort()
        rank=1
        for i in range(len(a)):
            if a[i] in freq:
                continue
            else:
                freq[a[i]]=rank
                rank+=1
        new_arr=[]
        for i in range(len(arr)):
            new_arr.append(freq[arr[i]])
        return new_arr                