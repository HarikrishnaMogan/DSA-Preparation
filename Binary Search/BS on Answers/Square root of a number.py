https://www.geeksforgeeks.org/problems/square-root/0?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=square-root

 def floorSqrt(self, n):
        l = 1
        h = n
        ans=1
        while l<=h:
            m=(l+h)//2
            #M*M gives the square product
            if m*m <= n:
                ans = m
                l=m+1
            else:
                h=m-1
        return ans
                
