class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        if nums[left]<=nums[right]:
            return nums[left]
        while left<right:
            tmp=left+(right-left)//2
            #print(tmp,left,right)
            if nums[tmp]>nums[right]:
                left=tmp+1
            else:
                right=tmp
        return nums[left]