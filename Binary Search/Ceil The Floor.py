https://www.geeksforgeeks.org/problems/ceil-the-floor2802/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=ceil-the-floor

class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        # code here
        # Floor of x is the largest element which is smaller than or equal to x. Floor of x doesn’t exist if x is smaller than smallest element of arr[].
# Ceil of x is the smallest element which is greater than or equal to x. Ceil of x doesn’t exist if x is greater than greatest element of arr[].
        arr.sort()
        #floor
        f =-1
        l =0 
        h = len(arr)-1
        while l<=h:
            m = (l+h)//2
            if arr[m] <= x:
                f = arr[m]
                l = m+1
            else:
                h = m-1
        #ceil
        c = -1
        l=0
        h=len(arr)-1
        while l<=h:
            m = (l+h)//2
            if arr[m] >= x:
                c=arr[m]
                h=m-1
            else:
                l = m+1
        return [f,c]
