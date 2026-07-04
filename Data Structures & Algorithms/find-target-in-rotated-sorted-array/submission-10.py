class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findPivot(nums):
            left,right=0, len(nums)-1
            if nums[left]<=nums[right]:
                return left
            while left<right:
                mid=left+(right-left)//2
                if nums[mid]<nums[right]:
                    right=mid
                else:
                    left=mid+1
            return left
        
        pp=findPivot(nums)
        #print(pp)
        left,right=0,len(nums)-1

        if target >= nums[pp] and target <= nums[right]:
            left=pp
        else:
            right=pp
        print(nums[left:right],pp,left,right)
        while left<=right:
            mid=left+(right-left)//2
            #print(mid,left,right)
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return -1


