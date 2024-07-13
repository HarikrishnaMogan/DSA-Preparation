https://leetcode.com/problems/reverse-integer/

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        r=0
        k =  abs(x)
        while k > 0:
            rem = k%10
            if r == 0:
                r = rem
            else:
                r = r*10 + rem
            k = k//10
        if x < 0:
            r = -1 * r
        else:
             r = r
        
        if r < -2**31 or r > 2**31-1:
            return 0
        else:
            return r
        
