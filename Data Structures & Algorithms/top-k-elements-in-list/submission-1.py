from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted=Counter(nums)     
        result=[]   
        for item in counted.most_common(k):
            result.append(item[0])
        return result