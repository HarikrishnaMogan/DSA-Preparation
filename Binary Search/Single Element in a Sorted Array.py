https://leetcode.com/problems/single-element-in-a-sorted-array/description/

   def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #index (even,odd) => single element is on the right half
        #index (odd,even) => single element is on the left half
        n=len(nums)
        if n ==1:
            return nums[0]
        if nums[0] !=nums[1]:
            return nums[0]
        if nums[n-1] != nums[n-2]:
            return nums[n-1]
        l =1
        h = n-2
        while l<=h:
            m=(l+h)//2
            #ans
            if nums[m] != nums[m-1] and nums[m] != nums[m+1]:
                return nums[m]
            
            #checking and eleminating based on Index(even,odd) logic
            if (m%2 !=0 and nums[m] == nums[m-1]) or (m%2==0 and nums[m]==nums[m+1]):
                l=m+1
            #checking and eliminating based on Index(odd,even) logic
            #(m%2!=0 and nums[m]==nums[m+1]) or (m%2==0 and nums[m] == nums[m-1])
            else:
                h=m-1
        
