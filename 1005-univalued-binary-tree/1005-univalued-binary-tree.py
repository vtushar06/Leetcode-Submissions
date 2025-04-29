# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        value=root.val
        def traverse(root,value):
            if root is None:
                return True
            if root.val !=value:
                return False
            return traverse(root.left,value) and traverse(root.right,value)
        return traverse(root,value)     
                   
        