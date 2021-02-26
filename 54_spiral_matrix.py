def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        R = len(matrix)
        C = len(matrix[0])
        x = 0
        ans = []
        
        visited = [False] * (R*C)
        while x < min(R, C):
            for i in range(x, C-x):
                if not visited[x*C + i]:    
                    ans.append(matrix[x][i])
                    visited[x*C + i] = True
                    
            
            for j in range(x+1,R-x):
                if not visited[j*C + C-x-1]:
                    ans.append(matrix[j][C-x-1])
                    visited[j*C + C-x-1] = True
            
            for k in range(C-x-2, x-1, -1):
                if not visited[(R-x-1)*C + k]:
                    ans.append(matrix[R-x-1][k])
                    visited[(R-x-1)*C + k] = True
            
            for l in range(R-x-2, x, -1):
                if not visited[l*C + x]:
                    ans.append(matrix[l][x])
                    visited[l*C + x] = True
                    
            
            x += 1
                
        return ans