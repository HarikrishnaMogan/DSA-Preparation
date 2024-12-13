https://leetcode.com/problems/divide-two-integers/description/

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == divisor:
            return 1
        
        sign = True
        if dividend > 0 and divisor < 0:
            sign = False
        if dividend < 0 and divisor > 0:
            sign = False
        
        
        n = abs(dividend)
        d = abs(divisor)
        ans=0
        while n >=d:
            count =0
            #(d<<(cnt+1)) is nothing but d*z**(count+1)
            while n >= (d<<(count+1)):
                count+=1
            ans+= 1<<count #1<<count is nothing but 2**(count)
            n = n-(d*(1<<count))  # subtracting n-(d*(2**count))
        if ans > 2**31-1 and sign:
            return 2**31-1
        if ans > 2**31 and not sign:
            return -2**31
        if sign:
            return ans
        else:
            return -1*ans
