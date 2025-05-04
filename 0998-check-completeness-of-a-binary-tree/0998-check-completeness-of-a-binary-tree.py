# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional,List
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        queue=deque([root])
        while(queue):
            node=queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
            else:
                break
        while(queue):
            if queue.popleft():
                return False
        return True                    
            
        