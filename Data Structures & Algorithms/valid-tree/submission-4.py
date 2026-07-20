class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodeMap = {}
        for i in range(n):
            nodeMap[i] = []
        
        for edge in edges:
            nodeMap[edge[0]].append(edge[1])
            nodeMap[edge[1]].append(edge[0])
            if edge[0] == edge[1]: return False
        print(nodeMap)
        
        visited = set()

        def dfs(node, prev):
            if node != prev and node in visited: return False

            visited.add(node)

            for nei in nodeMap[node]:
                if nei != prev:
                    if not dfs(nei, node): return False
            
            visited.remove(node)
            nodeMap[node] = []

            return True

        prev = 0
        node = 0
        if not dfs(node, prev): return False
        
        for node in range(n):
            if nodeMap[node] != []: return False
            

        
        return True