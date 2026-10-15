class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        curr=[]
        arr=[]
        candidates.sort()
        def f(i,ans):
            if ans==0:
                arr.append(curr[:])
                return 
            for j in range(i,len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if candidates[j] > ans:
                    break

                curr.append(candidates[j])
                f(j+1,ans-candidates[j])
                curr.pop()

        f(0,target)
        return arr       



             
              



        