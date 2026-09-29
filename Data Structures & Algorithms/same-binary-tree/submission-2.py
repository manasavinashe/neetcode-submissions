# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [[p, q]]
        while stack : 
            nodes = stack.pop()
            n0 = nodes[0]
            n1 = nodes[1]
            if n0 and n1 :
                if n0.val == n1.val : 
                    stack.append([n0.left,n1.left])
                    stack.append([n0.right,n1.right])
                    continue
                else : return False
            elif n0 or n1 :
                 return False 

        return True
        