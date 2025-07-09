# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Keep in mind that this tree is not in order

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        level = 0

        def depth_first_search(root,res,level):
            if root is None:
                return

            if len(res) <= level:
                res.append([])

            res[level].append(root.val)

            depth_first_search(root.left,res,level+1)
            depth_first_search(root.right,res,level+1)

        
        depth_first_search(root,res,level)
        final_res = [i[-1] for i in res]
        return final_res