https://leetcode.com/problems/binary-search/

   h = len(nums)-1
        l =0
        while l <= h:
            mid = (l+h)//2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                l = mid+1
            else:
                h = mid-1
        return -1
...............................................
 def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binarySearch(nums,l,h):
            if l > h:
                return -1

            mid = (l+h)//2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                return binarySearch(nums,mid+1,h)
            else:
                return binarySearch(nums,l,mid-1)
        return binarySearch(nums,0,len(nums)-1)
