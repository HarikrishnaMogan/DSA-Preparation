
https://www.geeksforgeeks.org/problems/count-total-set-bits-1587115620/1
 def countSetBits(self,n):
        # code here
        # return the count
        cnt = 0
        n=n+1 #so that we can include n as well
        x = 2 #initilaize as base power of 2
        
        #power of 2 should be lessthan n
        while x//2 < n:
            quotient = n//x #gives no of groups of 1s
            cnt+=quotient * (x//2)  #x//2 gives number of 1s in each group.so multipy with quotient gives total number of 1s
            
            #rem gives the left out bits in groups of 0 and 1
            rem = n%x
            #if rem > x//2 means, if rem is > than half of bits, then there may be some 1s left out
            if rem > x//2:
                cnt+= rem-(x//2) #subtracting the half bits with rem gives the remining set bits (1)
        
            x=x*2
        return cnt
