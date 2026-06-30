from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s=Counter(s1)
        left=0
        n=len(s2)
        while left<n:
            if s2[left] in s:
                right=left
                count={}
                while right<n and s2[right] in s:
                    if s2[right] in count:
                        count[s2[right]]=count[s2[right]]+1
                    else:
                        count[s2[right]]=1
                    right+=1
                    #print(count)
                    if count==s:
                        return True
            left+=1
        return False