https://www.geeksforgeeks.org/problems/generate-all-binary-strings/0

class Solution:
    def generateBinaryStrings(self, n):
        # Code here
        
        def generateBinary(str,n,arr):
            if len(str) == n:
                arr.append(str)
                return arr
            if str[-1] == '1':
                arr = generateBinary(str+'0',n,arr)
            else:
                arr =generateBinary(str+'0',n,arr)
                arr =generateBinary(str+'1',n,arr)
            return arr
        arr1 = generateBinary('0',n,[])
        arr2 = generateBinary('1',n,[])
        arr = arr1+arr2
        return arr
