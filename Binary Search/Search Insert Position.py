https://leetcode.com/problems/search-insert-position/description/

  def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        h = len(nums)-1
        ans = len(nums)
        while l<=h:
            m = (l+h)//2
            if nums[m] >= target:
                ans = m
                h = m-1
            else:
                l = m+1
        return ans
