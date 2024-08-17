https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1?track=DSASP-Searching&amp%253BbatchId=154&utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=floor-in-a-sorted-array

  #Complete this function
    def findFloor(self,A,N,X):
        #Your code here
        l = 0
        h = N-1
        ans = -1
        while l <=h:
            m = (l+h)//2
            if A[m] <= X:
                ans = m
                l = m+1
            else:
                h=m-1
        return ans
