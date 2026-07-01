class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1

        while left<=right:
            tmp=left+(right-left)//2
            if nums[tmp]==target:
                return tmp
            elif nums[tmp]<target:
                left=tmp+1
            else:
                right=tmp-1
        return -1