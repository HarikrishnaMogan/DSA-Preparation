
https://www.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=k-th-element-of-two-sorted-array

#User function Template for python3

class Solution:
    def kthElement(self, k, arr1, arr2):
        
        n1 = len(arr1)
        n2 = len(arr2)
        if n1 > n2: # use only small arry for n1,then only for single element this logic works assume n1 = [1], n2=[]
            return self.kthElement(k,arr2, arr1)
        
        low = max(0,k-n2)  #we should pick minimum of 1 element in arr1 if k>n2  # we won't have sufficentelements to form symmetry if we don't do this,assume k (10)is the last element and we don't have 10 elements to form symmentry  when mid1 is 0, o avoid that we make low as max of 0,k-n2
        high = min(k,n1)   # if k < n1 , it is practically not possible to pick maximim of n1 elements to form max of k elements # if simply k is 2nd element,and n2 is 4, we don't want to go till 4, we only need 2 elements max
        while low <=high:
            mid1 = (low+high)//2
            mid2 = k-mid1 #this gives other array mid2 or how many elements we need to consider in arr2
            l1 = float('-inf')
            l2 = float('-inf')
            r1 = float('inf')
            r2 = float('inf')
            
            if mid1 < n1:
                r1 = arr1[mid1]
            if mid2 < n2:
                r2 = arr2[mid2]
            if mid1-1 >=0:
                l1 = arr1[mid1-1]
            if mid2-1 >=0:
                l2=arr2[mid2-1]
            
            if l1<=r2 and l2<=r1:
                return max(l1,l2)
            elif l1 > r2:
                high = mid1-1
            else:
                low=mid1+1
        return 0
