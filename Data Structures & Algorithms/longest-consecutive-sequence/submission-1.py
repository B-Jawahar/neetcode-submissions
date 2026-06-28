class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_count=0
        nums=set(nums)
        seen=set()
        for num in nums:
            if num-1 not in nums:
                count=1
            else:
                continue
            if num in seen:
                continue
            else:
                seen.add(num)
            while num+1 in nums:
                seen.add(num+1)
                count+=1
                num+=1
            if count>max_count:
                max_count=count
        return max_count