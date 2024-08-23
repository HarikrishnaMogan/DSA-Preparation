
https://www.geeksforgeeks.org/problems/row-with-max-1s0023/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=row-with-max-1s
class Solution:
    def rowWithMax1s(self, arr):
        # code here
        maxcount = 0
        index = -1
        for i in range(len(arr)):
            
            #binary search on array
            low = 0
            high = len(arr[i])-1
            ans = len(arr[i])
            while low <=high:
                mid=(low+high)//2
                
                if arr[i][mid] >= 1:
                    ans = mid
                    high = mid-1
                else:
                    low = mid+1
            #calculating the count of 1's from index
            count = len(arr[i])-ans
            if count > maxcount:
                maxcount = count
                index = i
        return index
