# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def findifpossible(root,targetsum):
            if root is None:
                return False
            
            if (root.left is None and root.right is None ):
                return targetsum==root.val   
            remainingsum=targetsum-root.val     
            return findifpossible(root.left,remainingsum) or findifpossible(root.right,remainingsum)    
        return findifpossible(root,targetSum)        

        