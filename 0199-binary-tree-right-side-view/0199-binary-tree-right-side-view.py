# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional,List
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        bfs=[]
        queue=deque([root]) 
        while(queue):
            curr_size=len(queue)
            for i in range(curr_size):
                node=queue.popleft()
                if i==curr_size-1:
                    bfs.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return bfs                    

        
        