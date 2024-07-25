https://www.geeksforgeeks.org/problems/who-will-win-1587115621/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=who-will-win

def searchInSorted(self,arr, N, K):
        #Your code here
        i = 0
        j=N-1
        while i < j:
            if arr[i] == K:
                return 1
            if arr[j] == K:
                return 1
            i+=1
            j-=1
                
        return -1
