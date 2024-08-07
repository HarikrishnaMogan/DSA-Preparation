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
     #...........................................................

#optimized solution, TC - O(N), SC- O(1)
 # finding the most frequent element
        count1 = 0
        count2 = 0
        ele1 = float('-inf')
        ele2 = float('-inf')
        for i in nums:
            if count1 == 0 and ele2 != i:
                ele1 = i
                count1 =1
            elif count2 == 0 and ele1 != i:
                ele2 = i
                count2 =1
            elif ele1 == i:
                count1+=1
            elif ele2 == i:
                count2+=1
            else:
                count1-=1
                count2-=1
        # rechecking and verifying the element actual count
        count1 = 0
        count2 = 0
        ans = []
        for i in nums:
            if ele1 == i:
                count1+=1
            if ele2== i:
                count2+=1
        if count1 > len(nums)//3:
            ans.append(ele1)
        if count2 > len(nums)//3:
            ans.append(ele2)
        return ans
            
        
