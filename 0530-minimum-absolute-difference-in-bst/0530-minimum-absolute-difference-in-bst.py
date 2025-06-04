# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        newarr=[]
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            newarr.append(root.val)
            inorder(root.right)
        inorder(root) 
        newarr.sort()   
        mini=float("inf")
        for i in range(1,len(newarr)):
            mini=min(mini,abs(newarr[i]-newarr[i-1])  )
        return mini
        