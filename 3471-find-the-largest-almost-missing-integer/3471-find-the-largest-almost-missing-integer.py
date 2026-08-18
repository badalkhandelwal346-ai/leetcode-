class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        
        if k == len(nums):
            return max(nums)
        count=0
        total=0
        if k == 1:
            freq = Counter(nums)
            unique_nums = [x for x, count in freq.items() if count == 1]
            return max(unique_nums) if unique_nums else -1
        for i in range(len(nums)):
            if nums[i]==nums[0]:
                count+=1
            if nums[-1]==nums[i]:
                total+=1
        ans = -1

        if count == 1:
            ans = max(ans, nums[0])

        if total == 1:
            ans = max(ans, nums[-1])

        return ans

