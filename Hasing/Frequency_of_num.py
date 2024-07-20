
https://www.geeksforgeeks.org/problems/frequency-of-array-elements-1587115620/0

class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        # code here
        map = {}
        for i in range(0,N):
            if map.get(arr[i]):
                map[arr[i]]+=1
            else:
                map[arr[i]] =1
        for i in range(0,N):
            if map.get(i+1):
                arr[i] = map[i+1]
            else:
                arr[i] = 0
        return arr
            
