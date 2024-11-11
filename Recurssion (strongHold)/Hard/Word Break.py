https://leetcode.com/problems/word-break/description/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        #watch neetcode youtube solution for understanding
        dp= [False] *(len(s)+1)
        dp[len(s)] = True

        #check word from last character
        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if (i+len(w))<= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)] #initated dp[len(s)] = true, this will assign as true if the word matches and the track continues dynamiucally
                
                if dp[i]:
                    break
        return dp[0]
