class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen={}
        for word in strs:
            val="".join(sorted(word))
            if val in seen:
                l=seen[val]
                l.append(word)
                seen[val]=l
            else:
                l=[]
                l.append(word)
                seen[val]=l
        result=[]
        for val,key in seen.items():
            result.append(key)
        return result

