# Basic DFS: TC: O(2^(M+N)) SC O :(MN)
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs (matrix, i, j):
            ans = 0
            neighbours = [(0,1),(0,-1),(1,0),(-1,0)]
            for neighbour in neighbours:
                x = i + neighbour[0]
                y = j + neighbour[1]
                if x >= 0 and x < len((matrix)) and y >= 0 and y < len(matrix[0]) and matrix[x][y] > matrix[i][j]:
                    ans = max(ans, dfs(matrix, x, y))
            ans += 1
            return ans

        if not len(matrix):
            return 0
        ans = 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                ans = max(ans, dfs(matrix, i, j))
        return ans
    

# DFS + Memoization TC: O(MN) SC: O(MN)
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        neighbours = [(0,1),(0,-1),(1,0),(-1,0)]
        memory = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]

        def dfs (i, j):
            if memory[i][j] != 0:
                return memory[i][j] 
            for neighbour in neighbours:
                x = i + neighbour[0]
                y = j + neighbour[1]
                if x >= 0 and x < len((matrix)) and y >= 0 and y < len(matrix[0]) and matrix[x][y] > matrix[i][j]:
                    memory[i][j] = max(memory[i][j], dfs(x, y))
            memory[i][j] += 1
            return memory[i][j]

        if not len(matrix):
            return 0
        ans = 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                ans = max(ans, dfs(i, j))
        return ans