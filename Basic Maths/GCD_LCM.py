https://www.geeksforgeeks.org/problems/lcm-and-gcd4516/1

#according Eulier equilbirium
# GCD(a, b) = GCD(a-b, b) where a >b
# GCD(a,b) = GCD(a%b, b) where a > b
# lcm = a * b / gcd(a ,b)

class Solution:
    def lcmAndGcd(self, A , B):
        # code here 
        a = A
        b = B
        l = 0
        g =0
        while a > 0 and b > 0:
            if a > b:
                a = a%b
            else:
                b = b%a
        if a == 0:
            g = b
        else:
            g = a
        l = int((A*B)//g)
        return (l,g)
