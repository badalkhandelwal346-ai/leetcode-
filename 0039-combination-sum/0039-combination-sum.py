class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        per = []

        def f(target, i):

            if target == 0:
                ans.append(per.copy())
                return

            if target < 0 or i == len(candidates):
                return

            # Take
            per.append(candidates[i])
            f(target - candidates[i], i)
            per.pop()

            # Skip
            f(target, i + 1)

        f(target, 0)

        return ans