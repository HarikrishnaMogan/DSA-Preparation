
https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #if power of 2 only last bit is set as "1", remaining is zero ex:1000
        if n & n-1 == 0 and n!=0:
            return True
        return False
