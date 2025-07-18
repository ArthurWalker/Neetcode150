# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == q == None:
            return True
        elif p == None or q == None:
            return False
        else:
            if  (p.val == q.val):
                return self.isSameTree(p.left,q.left) and self.isSameTree(q.right,p.right)
            else:
                return False
        
        