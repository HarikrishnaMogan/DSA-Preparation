https://www.geeksforgeeks.org/problems/sum-of-first-n-terms5843/1

#using recursion
class Solution:
    def sumOfSeries(self,n):
        #code here
        if n == 0:
            return 0
        return n**3 + self.sumOfSeries(n-1)

#simple solution using formula
class Solution:
    def sumOfSeries(self,n):
        #code here
        return (n*(n+1)//2)**2
