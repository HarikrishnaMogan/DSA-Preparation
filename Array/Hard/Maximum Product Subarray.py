https://leetcode.com/problems/maximum-product-subarray/description/

 #if array has +ve values, then max product is product of all values
        #if array has even -ve values then max product is product of all values
        #if array has odd -ve values, then product of prefix or sufix has max product
        #if array has 0 , then omit zero and make prefix /sufix as 1, which ever encounter zero, becouse product zero woth any number always be zero
        prefix =1
        sufix =1
        n = len(nums)
        maxi = float('-inf')
        for i in range(n):
            if prefix == 0:
                prefix =1
            if sufix == 0:
                sufix = 1
            prefix *= nums[i]
            sufix*= nums[n-1-i]
            maxi = max(maxi,max(prefix,sufix)) 
        return maxi
