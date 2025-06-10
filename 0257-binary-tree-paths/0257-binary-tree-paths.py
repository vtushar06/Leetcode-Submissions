# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []

        def dfs(node, path):
            if not node:
                return
            # Add current node to the path
            path += str(node.val)
            # If it's a leaf, add to result
            if not node.left and not node.right:
                result.append(path)
            else:
                # Continue to children with '->'
                path += '->'
                dfs(node.left, path)
                dfs(node.right, path)

        dfs(root, "")
        return result

        