https://leetcode.com/problems/search-in-rotated-sorted-array/description/

  def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans = -1
        l = 0
        h=len(nums)-1
        while l<=h:
            m=(l+h)//2
            if nums[m] == target:
                return m
            elif nums[l] <= nums[m]: #check which half is sorted
                if nums[l] <= target and target <= nums[m]: #cchecking target present between the range, if present choose that range or eliminate the range
                    h=m-1
                else:
                    l=m+1
            else: # if above condition is not satistfied, then other half should be a sortred one i.e nums[h]>nums[m]
                if nums[m]<=target and target <=nums[h]:
                    l=m+1
                else:
                    h=m-1
        return ans 
