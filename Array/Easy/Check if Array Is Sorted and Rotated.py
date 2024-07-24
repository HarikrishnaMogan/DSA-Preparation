https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

 c = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                c+=1
        if nums[0] < nums[len(nums)-1]:
            c+=1
        if c <=1:
            return True
        else:
            return False
