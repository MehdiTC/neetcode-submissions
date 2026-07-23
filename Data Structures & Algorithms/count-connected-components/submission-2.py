class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        
        nodeMap = {}
        for i in range(n): nodeMap[i]=[]
        
        for edge in edges:
            nodeMap[edge[0]].append(edge[1])
            nodeMap[edge[1]].append(edge[0])

        visited = set()
        def dfs(node):
            if node in visited: 
                return 0
            
            visited.add(node)
            
            for n in nodeMap[node]:
                dfs(n)
            
            nodeMap[node] = []
            return 1
                
            
        for node in nodeMap:
            res+=dfs(node)
        
        return res
