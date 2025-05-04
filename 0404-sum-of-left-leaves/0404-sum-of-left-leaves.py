# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional,List
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        sum1=0
        queue=deque([])
        queue.append(root) 
        while(queue):
            curr_node=queue.popleft()
            if curr_node.left:
                if curr_node.left.left is None and curr_node.left.right is None:
                    sum1+=curr_node.left.val
                else:
                    queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)        
        return sum1            