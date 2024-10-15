https://leetcode.com/problems/count-good-numbers/description/



class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = int(10**9+7)
        def power(x,n,mod):
            
            if n == 0:
                return 1
            if n==1:
                return x%mod
            
            if n%2==0:
                return power(x*x,n//2,mod)%mod
            
            return (x*power(x,n-1,mod))%mod

        even = n//2+n%2
        odd = n//2
        return (power(5,even,mod)*power(4,odd,mod))%mod 

#.............................................................................
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = int(10**9+7)
        def power(x,n,mod):
            ans = 1
            while n > 0:
                if n%2 == 0:
                    x = (x*x)%mod
                    n=n//2
                else:
                    ans = ans*x
                    ans%=mod 
                    n=n-1
            return ans
                

        even = n//2+n%2
        odd = n//2
        return (power(5,even,mod)*power(4,odd,mod))%mod     
