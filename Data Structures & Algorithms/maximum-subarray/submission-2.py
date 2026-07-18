class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr=0
        currmax=0
        for i in nums:
            curr+=i
            if curr<0 or (curr==0 and i<0):
                curr=0
                #negmax=max(negmax,i)
            print(i,curr)
            currmax=max(curr,currmax)
        if currmax==0:    
            return max(nums)
        return currmax