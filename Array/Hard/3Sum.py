
#Better solution using hasmap and set
     ansSet = set()
        for i in range(len(nums)):
            map = set() #this can be hasmap/dict also
            for j in range(i+1,len(nums)):
                third = -(nums[i]+nums[j])
                if third in map:
                    temp = [nums[i],nums[j],third]
                    temp.sort()
                    ansSet.add(tuple(temp)) #cant able to add list , so used tuple
                map.add(nums[j])
        return list(ansSet) 
#......................................................
#most optimized solution
#three pointer
nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            while j < k:
                sum = nums[i]+nums[j]+nums[k]
                if sum < 0:
                    j=j+1
                elif sum > 0:
                    k = k-1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j < k and nums[j] == nums[j-1]:
                        j+=1
                    while j < k and nums[k] == nums[k+1]:
                        k-=1
        return ans

