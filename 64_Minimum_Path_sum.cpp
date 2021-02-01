class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        
        if(grid.empty())
            return 0;
        
        int rows = grid.size();
        int cols = grid[0].size();
        
        // fill the first row : here colum will be changing
        
        for(int i = 1 ; i < cols ; i++)
            grid[0][i] += grid[0][i-1];
        
        // fill the first col : here row will be changing
        
        for(int j = 1 ; j < rows ; j++)
            grid[j][0] += grid[j-1][0];
        
        
        for(int i = 1; i < rows ; i++){
            
            for(int j = 1; j < cols ; j++){
                
                grid[i][j]  += min(grid[i-1][j] , grid[i][j-1]);
            }
        }
        
           return grid[rows-1][cols-1];
    }
};