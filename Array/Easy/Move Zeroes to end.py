https://leetcode.com/problems/move-zeroes/description/

  def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0 
        j = 1
        while i < len(nums) and j < len(nums):
            if nums[i] == 0 and nums[j] != 0:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i+=1
                j+=1
            elif nums[i] != 0: #if i increment need to do j++, then only j will be ahead of i to compare and swap
                i+=1
                j+=1
            elif nums[j] == 0:
                j+=1
        return nums
