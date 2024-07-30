https://leetcode.com/problems/rearrange-array-elements-by-sign/

 def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = 0
        n= 1
        ans = [0]* len(nums)
        for i in nums:
            if i >= 0:
                ans[p] = i
                p+=2
            else:
                ans[n] = i
                n+=2
        return ans
