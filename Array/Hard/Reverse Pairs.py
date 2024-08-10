
https://leetcode.com/problems/reverse-pairs/
#TC - 2nLog(n), SC -O(n)

class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        h = len(nums)-1
        return self.mergeSort(nums,l,h)
    
    def countReversePairs(self,arr,l,m,h):
        right = m+1
        cnt=0
        for i in range(l,m+1):
            while right <= h and arr[i] > 2*arr[right]:
                right+=1
            cnt = cnt+(right-(m+1))
        return cnt
    
    def merge(self, arr, l, m, h):
        left = l 
        right=m+1
        temp =[]
        while left <= m and right <=h:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left+=1
            else:
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

    
    def mergeSort(self,arr, l, h):
        cnt = 0
        if l >= h:
            return cnt
        m = (l+h)//2
        cnt+= self.mergeSort(arr, l, m)
        cnt+= self.mergeSort(arr,m+1,h)
        cnt+= self.countReversePairs(arr,l,m,h)
        self.merge(arr,l,m,h)
        return cnt
