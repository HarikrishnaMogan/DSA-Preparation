
https://www.geeksforgeeks.org/problems/swap-two-numbers3844/1
class Solution:
    def get(self, a, b):
        #code here
        a = a^b
        b = a^b
        a = a^b
        return a,b
