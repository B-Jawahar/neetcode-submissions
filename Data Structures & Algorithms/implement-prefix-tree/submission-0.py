class TrieNode:
    def __init__(self):
        self.children=[None]*26
        self.isend=False
        
class PrefixTree:

    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        curr=self.root
        for c in word:
            index=ord(c)-ord('a')
            if curr.children[index] is None:
                curr.children[index]=TrieNode()
            curr=curr.children[index]
        curr.isend=True

    def search(self, word: str) -> bool:
        curr=self.root
        for c in word:
            index=ord(c)-ord('a')
            if curr.children[index] is None:
                return False
            curr=curr.children[index]
        if curr.isend is True:
            return True
        else:
            return False
                

    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for c in prefix:
            index=ord(c)-ord('a')
            if curr.children[index] is None:
                return False
            curr=curr.children[index]
        return True
        
        