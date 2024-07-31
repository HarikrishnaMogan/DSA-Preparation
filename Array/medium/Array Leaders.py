https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=leaders-in-an-array


 def leaders(self,n, arr):
        #Code here
        ans = [arr[len(arr)-1]]
        for i in range(len(arr)-2, -1, -1):
            if arr[i] >= arr[i+1] and arr[i] >= ans[len(ans)-1]:
                ans.append(arr[i])
        ans.reverse()
        return ans
