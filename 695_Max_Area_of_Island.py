class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        max_area = 0
        if not grid or not grid[0]:
            return 0

        def dfs(x,y):
            cur_area= 1
            for nx,ny in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
                if 0<=nx<row and 0<=ny<col and grid[nx][ny]==1: 
                    grid[nx][ny]=2
                    cur_area += dfs(nx,ny)

            return cur_area

        for x in range(row):
            for y in range(col):
                if grid[x][y]==1:
                    grid[x][y]=2
                    max_area=max(max_area,dfs(x,y))

        return max_area