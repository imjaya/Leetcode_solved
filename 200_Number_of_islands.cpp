class Solution {
private:
    const vector<vector<int>> DIR {{1,0}, {-1,0}, {0,1}, {0,-1}};
    
    bool isSafe(const vector<vector<char>>& grid, int x, int y) {
        return x >= 0 and x < grid.size() and y >= 0 and y < grid[0].size() and grid[x][y] == '1';
    }
    
    void markBfs(vector<vector<char>>& grid, int x, int y) {
        queue<array<int, 2>> q;
        q.push({x, y});
        while (!q.empty()) {
            auto current = q.front(); q.pop();
            for (const vector<int>& d : DIR) {
                int i = d[0] + current[0];
                int j = d[1] + current[1];
                if (isSafe(grid, i, j)) {
                    grid[i][j] = '0';
                    q.push({i, j});
                }
            }
        }
    }
    
public:
    int numIslands(vector<vector<char>>& grid) {
        int islands = 0;
        for (int i=0; i<grid.size(); i++) {
            for (int j=0; j<grid[0].size(); j++) {
                if (grid[i][j] == '1') {
                    markBfs(grid, i, j);
                    islands++;
                }
            }
        }
        return islands;
    }
};




//Approach

class Solution {
public:
  int numIslands(vector<vector<char>>& grid) {
    int nr = grid.size();
    if (!nr) return 0;
    int nc = grid[0].size();

    int num_islands = 0;
    for (int r = 0; r < nr; ++r) {
      for (int c = 0; c < nc; ++c) {
        if (grid[r][c] == '1') {
          ++num_islands;
          grid[r][c] = '0'; // mark as visited
          queue<pair<int, int>> neighbors;
          neighbors.push({r, c});
          while (!neighbors.empty()) {
            auto rc = neighbors.front();
            neighbors.pop();
            int row = rc.first, col = rc.second;
            if (row - 1 >= 0 && grid[row-1][col] == '1') {
              neighbors.push({row-1, col}); grid[row-1][col] = '0';
            }
            if (row + 1 < nr && grid[row+1][col] == '1') {
              neighbors.push({row+1, col}); grid[row+1][col] = '0';
            }
            if (col - 1 >= 0 && grid[row][col-1] == '1') {
              neighbors.push({row, col-1}); grid[row][col-1] = '0';
            }
            if (col + 1 < nc && grid[row][col+1] == '1') {
              neighbors.push({row, col+1}); grid[row][col+1] = '0';
            }
          }
        }
      }
    }

    return num_islands;
  }
};