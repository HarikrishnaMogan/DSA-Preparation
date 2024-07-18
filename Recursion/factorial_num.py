https://www.geeksforgeeks.org/problems/find-all-factorial-numbers-less-than-or-equal-to-n3548/0?problemType=functional&difficulty%255B%255D=-1&page=1&query=problemTypefunctionaldifficulty%255B%255D-1page1

#using o(k) time without recursion
class Solution:
    def factorialNumbers(self, n):
    	#code here 
    	x = 2
    	fact = 1
    	list = []
    	while fact <= n:
    	    list.append(fact)
    	    
    	    fact = fact*x
    	    x+=1
    	return list
............................................................................
#using recursion o(n) times
class Solution:
    def factorialNumbers(self, n):
    	#code here 
    	list = []
    	f=1
    	x=2
    	def fact(n,f, x):
    	    if n == 0:
    	        return
    	    list.append(f)
    	    f = f*x
    	    fact(n-1,f,x+1)
    	return list
