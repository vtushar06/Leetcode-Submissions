# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # def preorder_traversal(root):
        #     if root is None:
        #         return []
        #     left_side=preorder_traversal(root.left)
        #     right_side=preorder_traversal(root.right)    
        #     return [root.val]+left_side+right_side   
        def SearchBST(root,key):     
            if root is None:
                return None
            if root.val == key:
                return root
            if root.val<key:
                return SearchBST(root.right,key)
            else:  
                return SearchBST(root.left,key)
        return SearchBST(root,val)





        