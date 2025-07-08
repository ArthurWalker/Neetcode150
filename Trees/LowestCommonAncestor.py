# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# The key is that if both p and q less than root then we will search on the left
# while if both p and q more than root then we will search on the right
# If not above cases then the search will be splitted in at root and root is the common ancestor
# Edge case is even when p and q == root then root is still the common ancestor

# class Solution:
#     def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
#         if not root or not q or not p:
#             return None
        
#         curr = root
#         while curr:
#             if curr.val < p.val and curr.val < q.val:
#                 curr = curr.right
#             elif curr.val > p.val and curr.val > q.val:
#                 curr = curr.left
#             else:
#                 return curr


# Recursion:
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not q or not p:
            return None
        
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root


