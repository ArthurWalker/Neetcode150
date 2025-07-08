# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def postorder(root):
            if root == None:
                return 0

            left = postorder(root.left)
            right = postorder(root.right)
            if right == -1 or left == -1:
                return -1


            if abs(left-right) > 1:
                return -1
            return 1 + max(left,right)
        
        res = postorder(root)
        if res == -1:
            return False
        return True