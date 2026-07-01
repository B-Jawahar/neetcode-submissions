from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s=Counter(s1)
        s1len=len(s1)
        left=0
        n=len(s2)
        while (s1len+left-1)<n:
            if s2[left] in s:
                count={}
                #count[s2[left]]=1
                for i in range(s1len):
                    if s2[(left+i)] in count:
                        count[s2[(left+i)]]+=1
                    else:
                        count[s2[(left+i)]]=1
                #print(count,s)
                if count==s:
                    return True
                if s2[left+i] in s:
                    left+=1
                else:
                    left+=s1len
            else:
                left+=1
                #print(left)
        return False