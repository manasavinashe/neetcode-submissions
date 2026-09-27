# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int] : 
        if not root : 
            return []

        
        elements = []
        # left side 
        if root.left : 
            elements += self.inorderTraversal(root.left) 
        
        # append the value 
        elements.append(root.val) 

        # right side : 
        if root.right : 
            elements += self.inorderTraversal(root.right)
        
        return elements
        




        