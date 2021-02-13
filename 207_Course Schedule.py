class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq=collections.defaultdict(list)
        for c,p in prerequisites:
            prereq[p].append(c)
        # print(adjlist)
        
        def cycle(node,tracker,visited):
            tracker[node]=True
            visited[node]=True
            
            for n in prereq[node]:
                if n not in visited and cycle(n,tracker,visited):
                    return True
                elif n in tracker:
                    return True
            tracker.pop(node)
            return False
        visited={}
        for n in range(numCourses):
            tracker={}
            if n not in visited and cycle(n,tracker,visited):
                return False
        return True
            