# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indict={}
        for i,val in enumerate(inorder):
            indict[val]=i

        self.idx=0
        def tree(left,right):
            if left>right:
                return None
            val=preorder[self.idx]
            root=TreeNode(val)
            self.idx+=1
            mid=indict[val]
            root.left=tree(left,mid-1)
            root.right=tree(mid+1,right)
            return root
        return tree(0,len(preorder)-1)