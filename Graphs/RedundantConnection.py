class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        def dfs(cur,prev):
            if cur in visit:
                return True
            visit.add(cur)
            for adjs in graph[cur]:
                if adjs == prev:
                    continue
                is_cycle = dfs(adjs,cur)
                if  is_cycle:
                    return True
 
            return False
        
        graph = {i:[] for i in range(len(edges)+1)}
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            visit = set()
            if dfs(u,-1):
                return [u,v]
            
        return []
