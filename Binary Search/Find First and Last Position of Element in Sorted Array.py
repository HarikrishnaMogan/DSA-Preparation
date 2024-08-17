https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

   def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #first occurance
        first = -1
        l = 0
        h=len(nums)-1
        while l<=h:
            m = (l+h)//2
            if nums[m] == target:
                first = m
                h = m-1
            elif nums[m] < target:
                l = m+1
            else:
                h = m-1
        
        #last occurance
        l = 0
        h= len(nums)-1
        last = -1
        while l<=h:
            m = (l+h)//2
            if nums[m] == target:
                last = m
                l = m+1
            elif nums[m] < target:
                l = m+1
            else:
                h = m-1
        return [first,last]
