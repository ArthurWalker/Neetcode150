"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        # The goal is to create a node different from the original node and then create edge
        # To make this easier, having a hash to save previous visitted/created to avoid duplicate
        
        if not node:
            return None

        oldToNew = {}
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy_new_node = Node(node.val)
            oldToNew[node] = copy_new_node
            for neigh in node.neighbors:
                copy_new_node.neighbors.append(dfs(neigh))
            return copy_new_node

        return dfs(node)
