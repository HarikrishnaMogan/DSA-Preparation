

    def maxSubArray(self, nums):
       
       # this is kadanes algoritm
       # according to it if a sum is less than zero , make the sum as zero, since we only want maximun sum
       

        maxi = nums[0]
        sum = 0
        for i in nums:
            sum += i
            maxi = max(maxi, sum)
            if sum < 0: # make sum zero, if sum is negative
                sum =0
        return maxi
