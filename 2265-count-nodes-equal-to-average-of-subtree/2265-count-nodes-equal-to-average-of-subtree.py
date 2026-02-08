# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        
        def traverse(node):
            if not node:
                return 0, 0  # sum, count
            
            # Post-order: visit children first
            left_sum, left_count = traverse(node.left)
            right_sum, right_count = traverse(node.right)
            
            # Calculate current subtree metrics
            curr_sum = left_sum + right_sum + node.val
            curr_count = left_count + right_count + 1
            
            # Check the condition (integer division handles rounding down)
            if curr_sum // curr_count == node.val:
                self.count += 1
                
            return curr_sum, curr_count
        
        traverse(root)
        return self.count