# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxHeight(self,root:Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return 1+ max(self.maxHeight(root.left),self.maxHeight(root.right))


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        curr_left_height = self.maxHeight(root.left)
        curr_right_height = self.maxHeight(root.right)
        curr_diameter = curr_left_height + curr_right_height
        
        # Post-Traversal
        left = self.diameterOfBinaryTree(root.left)
        right = self.diameterOfBinaryTree(root.right)
        sub_height = max(left,right)

        return max(curr_diameter,sub_height)

# faster way:
class Solution:
    def __init__(self):
        self.dia = 0
    
    def postorder(self,root):
        if root == None:
            return 0
        left = self.postorder(root.left)
        right = self.postorder(root.right)
        self.dia = max(self.dia,left+right) # compare current depth with stored depth

        return 1+ max(left,right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.postorder(root)
        return self.dia