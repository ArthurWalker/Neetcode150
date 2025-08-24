class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False

        graph = {i: [] for i in range(n)}
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Draw adjency matrix
        # To know if a graph is circle then needs two trackers
        # 1/ have visit to track visitted node 
        # 2/ have prev to skip undirected edges (later on if adj == prev then continue)

        visit= set()
        def dfs(node,prev):
            if node in visit:
                return False
            
            visit.add(node)
            for adj in graph[node]:
                if adj == prev:
                    continue
                loop = dfs(adj,node)
                if not loop:
                    return False
            return True

        return dfs(0,-1) and len(visit) == n