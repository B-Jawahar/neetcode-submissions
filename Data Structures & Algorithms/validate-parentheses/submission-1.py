class Solution:
    def isValid(self, s: str) -> bool:
        lifo=[]
        if len(s)==0:
            return True
        for i in s:
            if len(lifo)>0 and lifo[-1]==i:
                lifo.pop()
            else:
                if i=="{":
                    lifo.append("}")
                elif i=="[":
                    lifo.append("]")
                elif i=="(":
                    lifo.append(")")
                else:
                    return False
        if len(lifo)>0:
            return False
        else:
            return True
                