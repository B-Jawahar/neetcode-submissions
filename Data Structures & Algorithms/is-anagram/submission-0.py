from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=list(s)
        l=list(t)
        if Counter(s)==Counter(l):
            return True
        else:
            return False