# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def binary_decimal(st):
            return int(st, 2)

        def sumtoLeaf(root, binary):
            if not root:
                return 0

            binary += str(root.val)

            # If it's a leaf node
            if not root.left and not root.right:
                return binary_decimal(binary)

            # Continue recursion
            return sumtoLeaf(root.left, binary) + sumtoLeaf(root.right, binary)

        return sumtoLeaf(root, "")


        