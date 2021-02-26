class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        n=len(matrix[0])
        result=[]
        for i in range(0,n):
            result.append(matrix[0][i])
        for i in range(1,m):
            result.append(matrix[i][-1])
        print(result)
        for i in range(m-1,0,-1):
            if(i%2==0):
                print(1)
                for j in range(n-2,-1,-1):
                    result.append(matrix[i][j])
                
            else:
                for j in range(0,n-1):
                    result.append(matrix[i][j])
                    
                    
        return result
                