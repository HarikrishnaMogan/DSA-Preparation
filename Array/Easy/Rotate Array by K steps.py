
https://leetcode.com/problems/rotate-array/description/
#k%len because, if len=k, then after doing k operations/ rotation the array will be same, so to avoid that added this
        k = k%len(nums)
        i = 0
        j= len(nums)-k-1

# reversing the first part
        while i < j:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i+=1
            j-=1
#reversing the second part
        i = len(nums)-k
        j = len(nums)-1
        while i < j:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i+=1
            j-=1
   #reversing the entire array     
        i =0
        j=len(nums)-1
        while i < j:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i+=1
            j-=1
        
        return nums
