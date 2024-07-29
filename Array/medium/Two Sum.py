
https://leetcode.com/problems/two-sum/


 def twoSum(self, nums, target):
        
        map = {}

        for i in range(len(nums)):
            rem = target-nums[i]
            if rem in map:
                return [i , map[rem]]
            map[nums[i]] = i

...........................................................
#used greedy approach , and sorting
      k = list(nums)
        k.sort()
        ans = []
        i=0
        j=len(nums)-1

        while i < j:
            sum = k[i]+k[j]
            if sum == target:
                ans =[k[i], k[j]]
                break
            elif sum < target:
                i+=1
            elif sum > target:
                j-=1

        ans[0] = nums.index(ans[0])
        nums[ans[0]] = -1 #added to modify the index, so that if an duplicate value there it wont affect result
        ans[1] = nums.index(ans[1])
        return ans
