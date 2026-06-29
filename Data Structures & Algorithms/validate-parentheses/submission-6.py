class Solution:
    def isValid(self, s: str) -> bool:
        lifo=[]
        for i in s:
            if lifo and lifo[-1]==i:
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
                