class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        seen = {}
        for req in prerequisites:
            seen.setdefault(req[0], []).append(req[1])

        visited = set()
        def dfs(crs):
            if not seen.get(crs): return True
            if crs in visited: return False

            visited.add(crs)
            for pre in seen.get(crs, []):
                if not dfs(pre): return False

            visited.remove(crs)
            seen[crs] = []
            return True   

        for crs in seen:
            if not dfs(crs): return False
        
        return True