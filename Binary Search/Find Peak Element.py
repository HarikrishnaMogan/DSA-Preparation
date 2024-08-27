https://leetcode.com/problems/find-peak-element/description/

def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n==1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[n-1]>nums[n-2]:
            return n-1
        l = 1
        h=n-2
        while l<=h:
            m=(l+h)//2

            if nums[m] > nums[m-1] and nums[m] > nums[m+1]:
                return m
            
            #check the mid if we are in increasing or decreasing slope
            #if increase slope, peak is on the right
            if nums[m] > nums[m-1]:
                l=m+1
            #if decrease slope, peak is on the left
            elif nums[m] > nums[m+1]:
                h=m-1    
            #if both cases won't have we have multiple peaks and we can either go to right or left
            else:
                h=m-1    
...........................................................................

#without edge cases outside and handling it inside

 n = len(nums)

        l = 0
        h=n-1
        while l<=h:
            m=(l+h)//2
            before= float('-inf')
            after= float('-inf')
            if m-1 >=0:
                before = nums[m-1]
            if m+1 < n:
                after = nums[m+1]
            if nums[m] > before and nums[m] > after:
                return m
            
            #check the mid if we are in increasing or decreasing slope
            #if increase slope, peak is on the right
            if nums[m] > before:
                l=m+1
            #if decrease slope, peak is on the left
            elif nums[m] > after:
                h=m-1    
            #if both cases won't have we have multiple peaks and we can either go to right or left
            else:
                h=m-1    
