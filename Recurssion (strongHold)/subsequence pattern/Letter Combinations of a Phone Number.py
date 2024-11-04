https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

        def comb(i,stri,ans,digits):
            if i == len(digits):
                ans.append(stri)
                return
            
            s = map[int(digits[i])]
            for char in s:
                comb(i+1,stri+char,ans,digits)
        ans=[]
        if not digits:
            return ans
        comb(0,"",ans,digits)
        return ans
