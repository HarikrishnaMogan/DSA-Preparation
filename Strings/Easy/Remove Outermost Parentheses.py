https://leetcode.com/problems/remove-outermost-parentheses/

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        outer = 0
        inner=0
        ans=""
        for i in range(len(s)):
            if outer == 0:
                outer+=1
                continue
            if s[i]=="(":
                inner+=1
                ans+="("
            elif inner != 0:
                inner-=1
                ans+=")"
            else:
                outer-=1
        return ans
