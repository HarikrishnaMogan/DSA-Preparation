https://leetcode.com/problems/fibonacci-number/

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        first = self.fib(n-1)
        last = self.fib(n-2)
        return first+last
