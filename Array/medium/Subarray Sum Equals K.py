
https://leetcode.com/problems/subarray-sum-equals-k/description/
        map = dict()
        c = 0
        sum = 0
        for i in range(len(nums)):
            sum+=nums[i]
            if sum == k:
                c+=1
            reminder = sum-k
            if reminder in map:
                c+=map[reminder]
            if sum in map:
                map[sum] += 1
            else:
                map[sum] = 1
        return c
