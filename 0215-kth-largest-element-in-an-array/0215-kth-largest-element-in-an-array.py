import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # nums=nums[::-1]
        # return nums[k-1]
        heap=[]
        for num in nums:
            heapq.heappush(heap,num)
        # for i in range(len(nums)-k):
        #     heapq.heappop(heap)
            if len(heap)>k:
                heapq.heappop(heap)
        return heap[0]        
