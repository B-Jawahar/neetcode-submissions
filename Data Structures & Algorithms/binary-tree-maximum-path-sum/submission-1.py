# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best=root.val

        def maxpath(node):
            nonlocal best
            if not node:
                return 0
            left=maxpath(node.left)
            right=maxpath(node.right)
            maxleft=max(left,0)
            maxright=max(right,0)
            nodeval=node.val+maxleft+maxright
            best=max(best,nodeval)

            return node.val+max(maxleft,maxright)
        maxpath(root)

        return best
