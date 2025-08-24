class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites)==0:
            return True

        graph = {i:[] for i in range(numCourses)} 
        for u,v in prerequisites:
            graph[v].append(u)

        def dfs(curr):
            if curr in visit:
                return False
            if graph[curr] == []:
                return True
            visit.add(curr)
            for adjs in graph[curr]:
                dup = dfs(adjs)
                if not dup:
                    return False
            graph[curr]=[]
            return True

        for c in range(numCourses):
            visit = set()
            is_cycle = dfs(c)
            if not is_cycle:
                return False
        return True