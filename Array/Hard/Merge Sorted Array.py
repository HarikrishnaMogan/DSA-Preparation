https://leetcode.com/problems/merge-sorted-array/


for i in range(m,len(nums1)):
            if i-m < len(nums2):
                nums1[i] = nums2[i-m]
            else:
                break
        nums1.sort()
#....................................
#optomized TC - O(m+n)
        last = m+n-1
        #merge from reverse
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m-=1
            else:
                nums1[last] = nums2[n-1]
                n-=1
            last-=1
        #join the leftover in nums2 if present
        while n > 0:
            nums1[last] = nums2[n-1]
            n-=1
            last-=1
