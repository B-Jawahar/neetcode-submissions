from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s=list(s)
        l=list(t)
        if Counter(s)==Counter(l):
            return True
        else:
            return False