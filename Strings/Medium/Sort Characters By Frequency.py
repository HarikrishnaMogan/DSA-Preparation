https://leetcode.com/problems/sort-characters-by-frequency/description/
class Solution:
    def frequencySort(self, s: str) -> str:
        map = {}

        for ch in s:
            if ch in map:
                map[ch] += 1
            else:
                map[ch] =1
        f = [(v,k) for k,v in map.items()]
        
        f.sort(key=lambda x:(-x[0],x[1]))
        ans=""
        for i in range(len(f)):
            if f[i][0] > 0:
                ans+=(f[i][1])*f[i][0]
        return ans
