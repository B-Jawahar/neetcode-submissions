# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        queue1=deque([p])
        queue2=deque([q])

        while queue1 and queue2:
            len1=len(queue1)
            len2=len(queue2)
            if len2!=len1:
                return False
            for _ in range(len1):
                node1=queue1.popleft()
                node2=queue2.popleft()
                if node1.val!=node2.val:
                    return False
                if node1.left and node2.left:
                    print("left1",node1.left.val)
                    print("left2",node2.left.val)
                    queue1.append(node1.left)
                    queue2.append(node2.left)
                else:
                    if node1.left or node2.left:
                        return False
                if node1.right and node2.right:
                    print("right1",node1.right.val)
                    print("right2",node2.right.val)
                    queue1.append(node1.right)
                    queue2.append(node2.right)
                else:
                    if node1.right or node2.right:
                        return False
        return True               

