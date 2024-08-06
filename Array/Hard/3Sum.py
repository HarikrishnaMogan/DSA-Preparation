
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
