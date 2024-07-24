
https://www.geeksforgeeks.org/problems/second-largest3735/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=second-largest

 def print2largest(self, arr):
        # Code Here
    
    
        max1 = float('-inf')
        max2 = float('-inf')
        
        for i in range(len(arr)):
            if arr[i] > max1:
                max2 = max1
                max1 = arr[i]
            elif arr[i] > max2 and  arr[i] != max1:
                max2 = arr[i]
        if max1 > max2 and max2 != float('-inf'):
            return max2
        else:
            return -1
