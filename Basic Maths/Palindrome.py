https://leetcode.com/problems/palindrome-number/

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        i =0
        while i < len(x)//2:
            if x[i] != x[len(x)-i-1]:
                return False
            i = i+1
        return True

        
