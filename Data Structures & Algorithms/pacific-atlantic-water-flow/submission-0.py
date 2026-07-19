class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    
        pac = set()
        atl = set()
        res=[]

        def isVal(r,c):
            if 0<=r<len(heights) and 0<=c<len(heights[0]): return True 
            return False

        def dfs(r,c, prevH, visited):
            if (r,c) in visited or prevH > heights[r][c]:
                return 
            
            visited.add((r,c))

            if isVal(r+1,c): dfs(r+1,c, heights[r][c], visited)
            if isVal(r-1,c): dfs(r-1,c, heights[r][c], visited)
            if isVal(r,c+1): dfs(r,c+1, heights[r][c], visited)
            if isVal(r,c-1): dfs(r,c-1, heights[r][c], visited)




        
        
        for r in range(len(heights)):
            dfs(r, 0, 0, pac)
            dfs(r, len(heights[0])-1, 0, atl)

        for c in range(len(heights[0])):
            dfs(0, c, 0, pac)
            dfs(len(heights)-1, c, 0, atl)

        


        for coord in pac:
            if coord in atl: res.append(list(coord))
        
        return res