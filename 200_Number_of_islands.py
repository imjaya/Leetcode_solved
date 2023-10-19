# DFS TC: O(M*N) SC: O(M*N)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(grid, i, j):
            grid[i][j] = "0"
            for neighbour in neighbours:
                x = i + neighbour[0]
                y = j + neighbour[1]
                if x >= 0 and x < len(grid) and y >=0 and y < len(grid[0]) and grid[x][y] =="1":
                    dfs(grid, x , y) 

        num_islands = 0
        for i in range(0, len(grid)):
            for j in range(0,len((grid[0]))):
                if grid[i][j] == "1":
                    num_islands += 1
                    dfs(grid, i, j)

        return num_islands
    
# BFS TC: O(M*N) SC: O(min(M, N))
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        count = 0

        def bfs(grid, q):
            while q:
                i, j = q.popleft()
                for neighbour in neighbours:
                    x = i + neighbour[0]
                    y = j + neighbour[1]
                    if x >= 0 and x < len(grid) and y >=0 and y < len(grid[0]) and grid[x][y] =="1":
                        grid[x][y] = "0"
                        q.append((x, y))

        q = deque()
        num_islands = 0
        for i in range(0, len(grid)):
            for j in range(0,len((grid[0]))):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    q.append((i, j))
                    bfs(grid, q)
                    num_islands += 1

        return num_islands
        
        