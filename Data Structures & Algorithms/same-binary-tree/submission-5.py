# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([(p,q)])
        while queue : 
            n0, n1 = queue.popleft()
            if n0 and n1 :
                if n0.val != n1.val : 
                    return False
                queue.append([n0.left, n1.left])
                queue.append([n0.right, n1.right])
            elif n0 or n1 :
                return False 
            
        return True
        
            

        