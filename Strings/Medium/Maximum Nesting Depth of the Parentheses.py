https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/
class Solution:
    def maxDepth(self, s: str) -> int:
        maxi = 0
        c=0
        for ch in s:
            if ch == "(":
                c+=1
            elif ch==")":
                c-=1
            maxi=max(maxi,c)
        return maxi
