class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        in_degree = collections.defaultdict(int)
        for u,v in prerequisites:
            graph[v].append(u)
            in_degree[u] += 1

        # init queue with indegree 0 nodes
        queue = collections.deque([ u for u in range(0, numCourses) if u not in in_degree])  # 0 to N, nodes list
        result = []
        while(queue):
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                result.append( node )
                for nei in graph[node]:
                    in_degree[nei] -= 1

                    if in_degree[nei] == 0:
                        queue.append( nei )
        return result if len(result) == numCourses else []
        