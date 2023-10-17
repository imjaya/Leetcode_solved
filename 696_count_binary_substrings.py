# Count groups of digit together and determine how many substring we can form for each adjacent group of smae characters which is min of the two groups length.
# TC: O(N) SC: O(N)

class Solution(object):
    def countBinarySubstrings(self, s):
        groups = [1]
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                groups.append(1)
            else:
                groups[-1] += 1

        ans = 0
        for i in range(1, len(groups)):
            ans += min(groups[i-1], groups[i])
        return ans
    

# Similar to above solution but in one single loop, linear scan. TC: O(N), SC: O(1)
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev, cur, result = 0, 1, 0

        for i in range(1, len(s)):
            if s[i] !=s[i-1]:
                result+=min(prev, cur)
                prev=cur
                cur=1
            else:
                cur+=1
        return result + min(prev,cur)
    
# Queue solution with sliding window(the while loop).
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        q = deque()
        count = 0
        for char in s:
            while q and q[-1] == char and q[0] != char:
                q.pop()
            if q and q[-1] != char:
                q.pop()
                count+=1
            q.appendleft(char)

        return count

        
        