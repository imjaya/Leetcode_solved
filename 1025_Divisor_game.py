class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        P = [0]*(N+1)
        
        for i in range(2, N + 1):
            for j in range(1, int(sqrt(i))+1):
                if i % j == 0 and P[i - j] == 0:
                    P[i] = 1
        print(P)
        return P[N]