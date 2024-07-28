
https://leetcode.com/problems/two-sum/


 def twoSum(self, nums, target):
        
        map = {}

        for i in range(len(nums)):
            rem = target-nums[i]
            if rem in map:
                return [i , map[rem]]
            map[nums[i]] = i
