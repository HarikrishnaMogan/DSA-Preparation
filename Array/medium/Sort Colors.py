https://leetcode.com/problems/sort-colors/

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

#three pointer or Dutch national falg algorithm
# intution:
# 0->low-1  = 0
#low -> mid-1 = 1
#mid -> high = unsorted(0,1,2 (any of these numbers))
#high+1 -> n-1 = 2


        low = 0
        mid = 0
        high = len(nums)-1

        while mid <= high:
            if nums[mid] == 0: # if mid is 0, swap to low, then increment the mid and low according to algo
                temp = nums[mid]
                nums[mid] = nums[low]
                nums[low] = temp
                low+=1
                mid+=1
            elif nums[mid] == 1: # if mid =1 , incrementing mid is enough according to algo range diagaram
                mid+=1
            else: # if mid =2, swap mid and high, decrement high
                temp = nums[mid]
                nums[mid] = nums[high]
                nums[high] = temp
                high-=1
        return nums
