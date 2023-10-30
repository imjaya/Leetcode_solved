#set approach TC: O(logN), SC: O(logN)
class Solution:
    def isHappy(self, n: int) -> bool:
        def digit_sum(num):
            total = 0
            while num > 0:
                d = num % 10
                num = num // 10
                total += d * d
            return total

        seen = set()
        while n not in seen and n != 1:
            print(n)
            seen.add(n)
            n = digit_sum(n)

        return n == 1
    
# Floyd cycle detection
#Instead of keeping track of just one value in the chain, we keep track of 2, called the slow runner and the fast runner. At each step of the algorithm, the slow runner goes forward by 1 number in the chain, and the fast runner goes forward by 2 numbers (nested calls to the getNext(n) function).
#If n is a happy number, i.e. there is no cycle, then the fast runner will eventually get to 1 before the slow runner.
#If n is not a happy number, then eventually the fast runner and the slow runner will be on the same number.
# TC: O(logn), SC: O(1)
class Solution:
    def isHappy(self, n: int) -> bool:
        def digit_sum(num):
            total = 0
            while num > 0:
                d = num % 10
                num = num // 10
                total += d * d
            return total

        slow_runner, fast_runner = n, digit_sum(n)
        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = digit_sum(slow_runner)
            fast_runner = digit_sum(digit_sum(fast_runner))
        return fast_runner == 1

