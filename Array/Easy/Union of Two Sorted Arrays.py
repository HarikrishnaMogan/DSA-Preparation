

https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=union-of-two-sorted-arrays
 def findUnion(self,arr1,arr2,n,m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        # code here 
        i = 0
        j =0
        ans=[]
        while i < n and j < m:
            k = len(ans)
    
            if arr1[i] <= arr2[j]:
                #for thr first time push elements
                if k == 0:
                    ans.append(arr1[i])
                #compare ans elements to push or not to avoid duplicates
                elif ans[k-1] != arr1[i]:
                     ans.append(arr1[i])
                #to avoid duplicates, if same, increment j as well
                if arr1[i] == arr2[j]:
                    j+=1
                i+=1
            else:
                if k == 0:
                     ans.append(arr2[j])
                elif ans[k-1] != arr2[j]:
                     ans.append(arr2[j])
                j+=1
                
        #push the remaining elements by comparing last elements in array
        while i  < n:
            k = len(ans)
            if ans[k-1] != arr1[i]:
                ans.append(arr1[i])
            i+=1
        while j < m:
            k = len(ans)
            if ans[k-1] != arr2[j]:
                ans.append(arr2[j])
            j+=1
        return ans
            
