https://leetcode.com/problems/4sum/

   nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:#need to avoid duplicate values
                continue
            for j in range(i+1,len(nums)):
                if j != i+1 and nums[j]== nums[j-1]:#need to avoid duplicate values
                    continue
                k = j+1
                l= len(nums)-1

                while k < l:
                    sum = nums[i]+nums[j]+nums[k]+nums[l]
                    if sum < target:
                        k+=1
                    elif sum > target:
                        l-=1
                    else:
                        temp = [nums[i],nums[j],nums[k],nums[l]]
                        ans.append(temp)
                        k+=1
                        l-=1

                        while k < l and nums[k] == nums[k-1]: #need to avoid duplicate values
                            k+=1
                        while k < l and nums[l]==nums[l+1]:#need to avoid duplicate values
                            l-=1
        return ans 
