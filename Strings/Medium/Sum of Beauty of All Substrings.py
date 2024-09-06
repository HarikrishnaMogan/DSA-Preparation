https://leetcode.com/problems/sum-of-beauty-of-all-substrings/

class Solution:
    def beautySum(self, s: str) -> int:
        
        n=len(s)
        if n==0:
            return 0

        def calBeauty(map):
            mini = float('inf')
            maxi = float('-inf')
            for i in map:
                if map[i] > 0:
                    mini = min(mini,map[i])
                    maxi=max(maxi,map[i])
            return maxi-mini


        beauty = 0
        for i in range(n):
            map={}
            for j in range(i,n):
                if s[j] in map.keys():
                    map[s[j]]+=1
                else:
                    map[s[j]]=1
                beauty += calBeauty(map)
        return beauty
                
