https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=inversion-of-array

 def inversionCount(self, arr, n):
        # Your Code Here
        
        def merge(arr,l,h):
            m = (l+h)//2
            left = l
            right = m+1
            temp=[]
            cnt = 0
            while left <= m and right <= h:
                if arr[left] <= arr[right]:
                    temp.append(arr[left])
                    left+=1
                else:
                    cnt +=m-left+1
                    temp.append(arr[right])
                    right+=1
            while left <=m:
                temp.append(arr[left])
                left+=1
            while right <=h:
                temp.append(arr[right])
                right+=1
                
            for i in range(l,h+1):
                arr[i] = temp[i-l]
            return cnt
                    
            
            
        def mergeSort(arr,l,h):
            cnt =0
            if l >=h:
                return cnt
            m = (l+h)//2
            cnt+=mergeSort(arr,l,m)
            cnt+=mergeSort(arr,m+1,h)
            cnt+=merge(arr,l,h)
            return cnt
        return mergeSort(arr,0,n-1)
        
                    
