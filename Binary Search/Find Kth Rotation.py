https://www.geeksforgeeks.org/problems/rotation4723/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=rotation


 def findKRotation(self, arr):
        # code here
        #min value index is the ans of how many times an array is rotated,
       # if we find minvalue in array it gives us the how many times an array is rotated
        l = 0
        h= len(arr)-1
        ans = float('inf')
        index = -1
        while l <=h:
            m=(l+h)//2
            
            if arr[l] <= arr[h]:
                if arr[l] < ans:
                    ans = arr[l]
                    index = l
                    break
            if arr[l] <= arr[m]:
                if arr[l]<ans:
                    ans=arr[l]
                    index = l
                l=m+1
            else:
                if arr[m]<ans:
                    ans=arr[m]
                    index=m
                h=m-1
        return index
