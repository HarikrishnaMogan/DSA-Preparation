
https://leetcode.com/problems/majority-element/

 def majorityElement(self, nums):
        
        #we can find the maximum frequency element by counting and decresing the count since the element is > n/2 times

        ele = None
        count = 0
        for i in nums:
            if count == 0: 
                ele = i
                count = 1
            elif ele != i:
                count -=1
            else:
                count+=1
        return ele
