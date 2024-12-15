https://leetcode.com/problems/single-number/description/

   def singleNumber(self, nums: List[int]) -> int:
        ans =0
        for i in nums:
            ans = i^ans
        return ans
