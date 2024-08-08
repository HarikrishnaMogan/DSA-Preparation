https://leetcode.com/problems/merge-sorted-array/


for i in range(m,len(nums1)):
            if i-m < len(nums2):
                nums1[i] = nums2[i-m]
            else:
                break
        nums1.sort()
#....................................
#optomized TC - O(m+n)
