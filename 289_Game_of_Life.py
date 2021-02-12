#space complexity(O(1))
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m=len(board)
        n=len(board[0])
        
        def isValidNeighbor(x, y):
            return x < len(board) and x >= 0 and y < len(board[0]) and y >= 0

        # All directions of neighbors
        x_dir = [-1, -1, -1, 0, 0, 1, 1, 1]
        y_dir = [-1,  0,  1, -1,1,-1, 0, 1]
        
        for row in range(0,m):
            for col in range(0,n):
                
                live_neighbors = 0
                for i in range(8):
                    curr_x, curr_y = row + x_dir[i], col + y_dir[i]
                    if isValidNeighbor(curr_x, curr_y) and abs(board[curr_x][curr_y]) == 1:
                        live_neighbors+=1
                
                # Rules 1 and 3: -1 indicates a cell that was live but now is dead.
                if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = -1
                    
                # Rule 4: 2 indicates a cell that was dead but now is live.
                if board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 2
                 
        # Get the final board
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] >= 1:
                    board[row][col] = 1
                else:
                    board[row][col] = 0