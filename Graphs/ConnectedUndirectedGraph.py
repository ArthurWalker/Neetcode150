class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visitted = [False]*n

        # Group and display graphs in a understandable manner. Use either dict or list, however, for list, it is more efficient memory and loop
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # connected_node = {}
        # for edge in edges:
        #     if edge[0] not in connected_node:
        #         connected_node[edge[0]] = [edge[1]]
        #     else:
        #         connected_node[edge[0]].append(edge[1])
        #     if edge[1] not in connected_node:
        #         connected_node[edge[1]] = [edge[0]]
        #     else:
        #         connected_node[edge[1]].append(edge[0])
        
        # print(connected_node)

        # if len(connected_node) == 0:
        #     return n

        # Use either DFS or BFS to travel through each node to determine graph
        def dfs(node):
            for neigh in adj[node]:
                if not visitted[neigh]:
                    visitted[neigh] = True
                    dfs(neigh)

        def bfs(node):
            q = [node]
            visitted[node] = True
            while q:
                curr = q.pop(0)
                for neigh in adj[curr]:
                    if not visitted[neigh]:
                        visitted[neigh] = True
                        q.append(neigh)

        res = 0
        for node in range(n):
            if not visitted[node]:
                visitted[node] = True
                dfs(node)
                res+=1
        return res        
