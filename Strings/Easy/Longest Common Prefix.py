https://leetcode.com/problems/longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        for i in range(len(strs[0])):
            for s in strs:
                if i== len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
..........................................
#optimised , O(nlogn)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first = strs[0]
        last=strs[-1]
        res=""
        for i in range(min(len(first),len(last))):
            if first[i] != last[i]:
                return res
            res+=first[i]
        return res
