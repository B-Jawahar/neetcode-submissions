# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        queue=deque([root])
        result=[]
        while queue:
            ls=len(queue)
            level=[]

            for _ in range(ls):
                node=queue.popleft()
                if node:
                    #print(node.val)
                    level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            print(level)
            result.append(level)
        return result