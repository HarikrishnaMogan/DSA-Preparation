https://leetcode.com/problems/roman-to-integer/submissions/1378379496/

class Solution:
    def romanToInt(self, s: str) -> int:
        def getMap(ch):
            if ch == "I":
                return 1
            elif ch == "V":
                return 5
            elif ch == "X":
                return 10
            elif ch == "L":
                return 50
            elif ch == "C":
                return 100
            elif ch == "D":
                return 500
            elif ch == "M":
                return 1000
            else:
                return 0
        ans=0
        prev =0 
        for i in range(len(s)-1,-1,-1):
            val = getMap(s[i])
            if prev <=val:
                ans = ans+val
            elif prev > val:
                ans = ans-val
            prev = val
        return ans
