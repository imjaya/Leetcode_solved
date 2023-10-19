#BFS solution TC: O(N*M) , SC: O(N)
class Solution:

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        neighbours = collections.defaultdict(list)
        for i in range(0, len(equations)):
            neighbours[equations[i][0]].append([equations[i][1], values[i]])
            neighbours[equations[i][1]].append([equations[i][0], 1 / values[i]])

        def bfs(src, target):
            if src not in neighbours or target not in neighbours:
                return -1
            q, visited = deque(), set()
            q.append([src, 1])
            while q:
                node, w = q.popleft()
                if node == target:
                    return w
                for neighbour, weight in neighbours[node]:
                    if neighbour not in visited:
                        q.append([neighbour, w*weight])
                        visited.add(neighbour)
            return -1


        
        return [bfs(query[0], query[1]) for query in queries]