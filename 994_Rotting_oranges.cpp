class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int m=grid.size();
        int n=grid[0].size();
        queue<pair<int,int>> rotten;
        int fresh=0;
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(grid[i][j]==2)
                {
                    rotten.push({i,j});
                }
                else if(grid[i][j]==1)
                {
                    fresh+=1;
                }
            }
        }
        if(fresh==0)
        {
            return(0);
        }
        int minutes=0;
        while (!rotten.empty() && fresh)
        {
            int l =rotten.size();
            while(l){
                l=l-1;
                int i=0,j=0;
                i=rotten.front().first;
                j=rotten.front().second;
                rotten.pop();
                if(i > 0 && grid[i - 1][j] == 1){
                    grid[i - 1][j] = 2;
                    rotten.push({i - 1, j});
                    fresh -= 1;
                    }
                if(i < grid.size() - 1 && grid[i + 1][j] == 1){
                    grid[i + 1][j] = 2;
                    rotten.push({i + 1, j});
                    fresh -= 1;
                    }
                if(j > 0 && grid[i][j - 1] == 1){
                    grid[i][j - 1] = 2;
                    rotten.push({i, j - 1});
                    fresh -= 1;
                    }
                if(j < grid[0].size() - 1 and grid[i][j + 1] == 1){
                    grid[i][j + 1] = 2;
                    rotten.push({i, j + 1});
                    fresh -= 1;
                    }
                
                   
                }
            minutes+=1;  
            
                 }
        
        
            if(fresh)
            {
                return(-1);
            }
            return(minutes);
        
        
    }
};