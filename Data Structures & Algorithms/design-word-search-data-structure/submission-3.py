class TrieNode:
    def __init__(self):
        self.children=[None]*26
        self.isend=False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        curr=self.root
        for c in word:
            idx=ord(c)-ord('a')
            if curr.children[idx] is None:
                curr.children[idx]=TrieNode()
            curr=curr.children[idx]
        curr.isend=True

    def search(self, word: str) -> bool:
        #curr=self.root

        def dfs(i,curr):
            for c in range(i,len(word)):
                if word[c]=='.':
                    for val in curr.children:
                        if val is not None and dfs(c+1,val):
                            return True
                    return False
                else:
                    idx=ord(word[c])-ord('a')
                    print(word[c],idx)
                    if curr.children[idx] is None:
                        return False
                    curr=curr.children[idx]
            if curr.isend is True:
                return True
            else:
                return False
        return dfs(0,self.root)
