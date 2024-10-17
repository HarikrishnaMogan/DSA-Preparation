https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def paran(s,open,close,n,ans):
            if open > n:
                return
            if open+close == 2*n and open == close:
                ans.append(s)
                return ans
            
            paran(s+"(",open+1,close,n,ans)
            if open > close:
                paran(s+")",open,close+1,n,ans)
            return ans
        return paran("(",1,0,n,[])
