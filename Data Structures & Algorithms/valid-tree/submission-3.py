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
            print(f"node = {node} | prev = {prev} | visited = {visited}")
            if node != prev and node in visited: return False

            visited.add(node)

            for nei in nodeMap[node]:
                if nei != prev:
                    print(f"Im gonna look at {nei}")
                    if not dfs(nei, node): return False
                else:
                    print(f"Im not gonna look at {nei} cos prev is {prev}")
            
            visited.remove(node)
            nodeMap[node] = []


            return True

        prev = 0
        node = 0
        if not dfs(node, prev): return False
        
        for node in range(n):
            if nodeMap[node] != []: return False
            

        
        return True