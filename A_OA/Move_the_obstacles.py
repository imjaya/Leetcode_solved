from collections import deque  
def solution(m):
    if len(m) == 0 or len(m[0]) == 0:
        return -1  # impossible

    matrix = [row[:] for row in m]
    # print(matrix)
    nrow, ncol = len(matrix), len(matrix[0])

    q = deque([((0, 0), 0)])  # ((x, y), step)
    matrix[0][0] = 0
    while q:
        # print(q)
        (x, y), step = q.popleft()

        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            if 0 <= x+dx < nrow and 0 <= y+dy < ncol:
                if matrix[x+dx][y+dy] == 9:
                    return step+1
                elif matrix[x+dx][y+dy] == 1:
                    # mark visited
                    matrix[x + dx][y + dy] = 0
                    q.append(((x+dx, y+dy), step+1))

    return -1
    
lot = [
[1, 0, 0],
[1, 0, 9],
[1, 9, 1]]
# lot = [
# [1, 0],
# [1, 9],
# [1, 9]]
# lot=[[]]
print(solution(lot))

