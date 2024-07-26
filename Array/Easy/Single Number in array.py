
https://leetcode.com/problems/single-number/description/
 ans =0
        for i in nums:
            ans = ans^i
        return ans
