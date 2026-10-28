class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        freq={}
        for i in range(len(arr)):
            if arr[i] in freq:
                freq[arr[i]]+=1
            else:
                freq[arr[i]]=1
        freq=sorted(freq.items(), key=lambda x: x[1], reverse=True)

        # return freq
        count=0
        total=0
        for i in range(len(freq)):
            count+=freq[i][1]
            total+=1  
            if count>=len(arr)//2:
                return total
             
            

            


