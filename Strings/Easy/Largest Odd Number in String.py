https://leetcode.com/problems/largest-odd-number-in-string/description/

class Solution:
    def largestOddNumber(self, num: str) -> str:
        index = -1
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2 !=0:
                index=i
                break;
        if index !=-1:
            return num[:index+1]
        else:
            return ""  
