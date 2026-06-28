class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)==0:
            return "0"
        l=[]
        for word in strs:
            w=[]
            for ch in word:
                w.append(str(ord(ch)))
            l.append("_".join(w))
        return "__".join(l)

    def decode(self, s: str) -> List[str]:
        if s=="0":
            return []
        w=s.split("__")
        decoded_list=[]
        for word in w:
            l=word.split("_")
            final_word=[]
            for ch in l:
                #return l
                if ch:
                    final_word.append(chr(int(ch)))
            decoded_list.append("".join(final_word))
        return decoded_list
