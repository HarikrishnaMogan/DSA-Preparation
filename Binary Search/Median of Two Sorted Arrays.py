https://leetcode.com/problems/median-of-two-sorted-arrays/description/


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2= len(nums2)
        if n1 > n2 :
            return self.findMedianSortedArrays(nums2,nums1)  #only take smaller for n1, otherwise this logic won't work for n1 having one element and n2 having no elements.
        left = (n1+n2+1)//2 #finding the left half 
        totalLength = n1+n2
        low = 0
        high = n1
        while low <= high:
            mid1 = (low+high)//2
            mid2 = left - mid1
            l1 = float('-inf')
            l2=float('-inf')
            r1 = float('inf')
            r2 = float('inf')
            if mid1 < n1:
                r1 = nums1[mid1]
            if mid2 < n2:
                r2 = nums2[mid2]
            if mid1-1 >=0:
                l1 = nums1[mid1-1]
            if mid2-1 >=0:
                l2=nums2[mid2-1]

            if l1 <= r2 and l2 <= r1:
                if totalLength%2 != 0:
                    median = max(l1,l2)
                    return median
                else:
                    median = (max(l1,l2)+min(r1,r2))/2
                    return median
            elif l1 > r2:
                high = mid1-1
            else:
                low = mid1+1
        return 0



        
