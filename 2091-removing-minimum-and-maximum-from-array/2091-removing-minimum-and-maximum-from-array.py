class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:

        n=len(nums)
        minimum=100000
        maxi_ind=0
        mini_ind=0
        maximum=-100000
        
        for i in range(len(nums)):
            if nums[i]>maximum:
                maximum=nums[i]
                maxi_ind=i
            if nums[i]<minimum:
                minimum=nums[i]
                mini_ind=i
        left=max(mini_ind,maxi_ind)+1
        right=n-min(mini_ind,maxi_ind)
        a1=(mini_ind+1)+(n-maxi_ind)
        a2=(maxi_ind+1)+(n-mini_ind)
        return min(left,right,a1,a2)

            