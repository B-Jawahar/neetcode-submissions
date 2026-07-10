# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        left=0
        right=0

        def height(root):
            if not root:
                return [True,0]
            left=height(root.left)
            right=height(root.right)
            balanced=left[0] and right[0] and abs(left[1]-right[1])<=1
            if balanced==False:
                return [False,0]
            return [balanced,1+max(left[1],right[1])]

        return height(root)[0]
        