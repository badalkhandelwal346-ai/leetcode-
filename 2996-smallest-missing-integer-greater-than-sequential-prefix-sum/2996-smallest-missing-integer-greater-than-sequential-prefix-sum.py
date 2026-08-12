class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        total = nums[0]

        # Find sum of longest sequential prefix
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            total += nums[i]
            i += 1

        # Put all numbers in a set for fast lookup
        nums_set = set(nums)

        # Find smallest missing integer >= total
        while total in nums_set:
            total += 1

        return total