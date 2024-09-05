https://leetcode.com/problems/string-to-integer-atoi/
class Solution:
    def myAtoi(self, s: str) -> int:
        ans=None
        pos=1
        sign = False
        s= s.strip()

        if len(s) == 0:
            return 0

        for i in range(len(s)):
            if i== 0 and s[i]=="-":
                pos=-1
                continue
            
            if i==0 and s[i]=="+":
                pos=1
                continue
                
            if s[i].isnumeric():
                if ans==None:
                    ans=s[i]
                else:
                    ans+=s[i]
            else:
                break

        if ans==None:
            return 0
        elif (int(ans)*pos) < -2**31:
            return -2**31
        elif (int(ans)*pos) > 2**31-1:
            return 2**31-1
        else:
            return int(ans)*pos 
