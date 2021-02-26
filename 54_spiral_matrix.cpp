class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> res;
        int row = matrix.size() - 1;
        int col = matrix[0].size() - 1;
        for(int i = 0, j = 0; i <= row && j <= col; i++, j++){
            //get top
            for(int k = j; k <= col; k++){
                res.push_back(matrix[i][k]);
            }
            if(i == row) return res; //when i == row there is only one row left 
            
            // get right
            for(int k = i + 1; k <= row; k++){
                res.push_back(matrix[k][col]);
            }
            if(j == col) return res; //when j == col there is only one col left
            
            // get bottom
            for(int k = col - 1; k >= j; k--){
                res.push_back(matrix[row][k]);
            }
            
            //get left
            for(int k = row - 1; k > i; k--){
                res.push_back(matrix[k][i]);
            }
            row--, col--;
        }
        
        return res;
    }
};