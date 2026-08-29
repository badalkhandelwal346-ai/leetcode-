class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        li=[]
        def starting(start,end):
            ans=-1
            while start<=end:
                mid=(start+end)//2
                if nums[mid]==target:
                    ans=mid
                    end=mid-1
                elif nums[mid]>target:
                    end=mid-1    
                else:
                    start=mid+1
            return ans
        def ending(start,end):
            ans=-1
            while start<=end:
                mid=(start+end)//2
                if nums[mid]==target:
                    ans=mid
                    start=mid+1
                elif nums[mid]>target:
                    end=mid-1    
                else:
                    start=mid+1
            return ans
        li.append(starting(0,len(nums)-1))
        li.append(ending(0,len(nums)-1))
        return li                                  
        