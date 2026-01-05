# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.totalSum = 0

        def reverseInorder(node):
            if not node:
                return
            
            # Visit right subtree first
            reverseInorder(node.right)
            
            # Update current node
            self.totalSum += node.val
            node.val = self.totalSum
            
            # Visit left subtree
            reverseInorder(node.left)

        reverseInorder(root)
        return root