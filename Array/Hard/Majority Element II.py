https://leetcode.com/problems/majority-element-ii/

#my solution, TC - O(nlog(n)), sc-O(1)

 nums.sort()
        ans = []
        ele = nums[0]
        count = 0
        majority = len(nums)//3
        for i in nums:
            if ele == i:
                count+=1
            else:
                if count > majority:
                    ans.append(ele)
                count = 1
                ele = i
        if count > majority:
            ans.append(ele)
        return ans
        
