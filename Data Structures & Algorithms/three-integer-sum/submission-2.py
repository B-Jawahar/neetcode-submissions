class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        #return nums
        n=len(nums)
        for i,num in enumerate(nums):
            if i>0 and nums[i]==nums[i-1]:
                continue
            else:
                target=num
                left=i+1
                right=n-1

                
                while left<right:
                    tmp=target+nums[left]+nums[right]

                    if tmp>0:
                        right-=1
                    elif tmp<0:
                        left+=1
                    else:
                        result.append((num,nums[left],nums[right]))
                        left+=1
                        right-=1
                        while left<right and nums[left]==nums[left-1]:
                            left+=1
                        while left<right and nums[right]==nums[right+1]:
                            right-=1
        return result
