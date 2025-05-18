# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue=deque([[root,1,1]])
        prevlevel=0
        start_num=1
        maxwidth=0
        while(len(queue)):
            [node,num,level]=queue.popleft()
            if level>prevlevel:
                prevlevel=level
                start_num=num

            maxwidth=max(maxwidth,num-start_num+1)
            if node.left:
                queue.append([node.left,2*num,level+1])
            if node.right:
                queue.append([node.right,2*num+1,level+1])
        return maxwidth                
        