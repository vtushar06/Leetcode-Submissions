# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_balance(node):
            if not node:
                return 0  # height of empty subtree is 0
            
            left_height = check_balance(node.left)
            if left_height == -1:
                return -1  # left subtree not balanced
            
            right_height = check_balance(node.right)
            if right_height == -1:
                return -1  # right subtree not balanced
            
            if abs(left_height - right_height) > 1:
                return -1  # current node not balanced
            
            return max(left_height, right_height) + 1  # height of subtree rooted at this node
        
        return check_balance(root) != -1