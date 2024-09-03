
https://leetcode.com/problems/valid-anagram/description/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        arr=[0]*26
        for i in range(len(s)):
            arr[ord(s[i])-ord('a')]+=1
            arr[ord(t[i])-ord('a')]-=1
        for i in arr:
            if i!=0:
                return False
        return True
        
