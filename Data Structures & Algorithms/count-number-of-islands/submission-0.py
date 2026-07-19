class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        islands = 0

        def isValid(i,j):
            if 0<=i<len(grid) and 0<=j<len(grid[0]): return True
            return False

        def dfs(i, j):
            if (i,j) in seen or grid[i][j]=="0":
                return
            
            seen.add((i,j))

            if isValid(i+1, j): dfs(i+1,j)
            if isValid(i-1, j): dfs(i-1,j)
            if isValid(i, j+1): dfs(i,j+1)
            if isValid(i, j-1): dfs(i,j-1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in seen:
                    islands += 1
                    dfs(i,j)
        
        return islands
        