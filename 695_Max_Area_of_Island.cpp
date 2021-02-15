class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
      int m = 0, xs = grid[0].size(), ys = grid.size();
  
      for(int x = 0; x < xs ; x++)
        for(int y = 0; y < ys ; y++)                     //search in our array 1 
          if(grid[y][x]){                                //if find out
            queue <pair<int,int>> q;                     //queue for BFS (as visited will use our array: 0 - is visited)
            int tmp = 0;                                 //area for current island 
            q.push({x,y});
            while(!q.empty()){                           //BFS
              int xx = q.front().first, yy = q.front().second;q.pop();
              if(!grid[yy][xx]) continue;                //if visited 
              tmp++;                                     //if not
              grid[yy][xx] = 0;                          //check current cell as visited 
              if(yy > 0 and grid[yy-1][xx]) q.push({xx,yy-1});             //for next level of BFS
              if(yy < ys - 1 and grid[yy+1][xx]) q.push({xx,yy+1});
              if(xx > 0 and grid[yy][xx-1]) q.push({xx-1,yy});
              if(xx < xs - 1 and grid[yy][xx+1]) q.push({xx+1,yy});
            }
            if(tmp > m) m = tmp;                  //check current area and previous maximal area
          } 
      
      return m;    
    }
};