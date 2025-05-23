# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional,List
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:return []
        bfs=[]
        queue=deque([])
        queue.append(root)
        left_to_right=True
        while( len(queue)!=0):
            curr_level_size=len(queue)
            curr_level=[]
            for i in range(curr_level_size):
                curr_node=queue.popleft()
                curr_level.append(curr_node.val) 
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            if left_to_right==False:
                curr_level.reverse()
            bfs.append(curr_level)
            left_to_right=not left_to_right
        return bfs                         