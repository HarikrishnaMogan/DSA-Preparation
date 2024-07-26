https://leetcode.com/problems/missing-number/

  sum1 = (len(nums)*(len(nums)+1))/2  #n*(n+1)/2 sum of n numbers
        sum2 =0
        for i in nums:
            sum2 += i
        return sum1-sum2 

..................................................

using XOR
Two important properties of XOR are the following:
XOR of two same numbers is always 0 i.e. a ^ a = 0. ←Property 1.
XOR of a number with 0 will result in the number itself i.e. 0 ^ a = a.  ←Property 2

Approach:
The steps are as follows:

We will first run a loop(say i) from 0 to N-2(as the length of the array = N-1).
Inside the loop, xor2 variable will calculate the XOR of array elements
i.e. xor2 = xor2 ^ a[i].
And the xor1 variable will calculate the XOR of 1 to N-1 i.e. xor1 = xor1 ^ (i+1).
After the loop ends we will XOR xor1 and N to get the total XOR of 1 to N.
Finally, the answer will be the XOR of xor1 and xor2.

 xor1 = 0
        xor2 =0
        for i in range(1, len(nums)+1):
            xor1 =xor1^i
            xor2 = xor2^nums[i-1]
        return xor1^xor2
