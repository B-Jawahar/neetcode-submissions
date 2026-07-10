# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(root):
            if not root:
                return root
            if root.left or root.right:
                left=root.left
                right=root.right
                root.left=right
                root.right=left
                #print(root.left.val,root.right.val)
                invert(root.left)
                invert(root.right)
            else:
                return root
        invert(root)
        return root