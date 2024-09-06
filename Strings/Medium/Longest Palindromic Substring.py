https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n==0:
            return ""
        start=0
        maxi=0
        for i in range(n):

            #i+0 -> odd palindrome
            #i+1 -> even palindrome
            for j in range(2):
                low = i
                high = i+j
                while low >=0 and high < n and s[low]==s[high]:
                    currlen = high-low+1
                    if currlen > maxi:
                        start=low
                        maxi=currlen 
                    low-=1
                    high+=1
        return s[start:start+maxi]
