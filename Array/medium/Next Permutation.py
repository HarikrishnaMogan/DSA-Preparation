https://leetcode.com/problems/next-permutation/description/

class Solution(object):
    def nextPermutation(self, nums):

        #Like longest prefix in dictionary ,find the break point, arr[i] < arr[i+1], store the i index
        #find the smallest large number greater than break point index value and swap.
        # we know the values after breakpoint are in the increasing order from end, so reverse it
        # once completed we get the next permutation


#finding the break point index
        i =len(nums)-2
        index = -1
        while i >= 0:
            if nums[i] < nums[i+1]:
                index = i
                break
            i-=1
# swaping the index value with smallest large element greter than break point value
# to do that we are searching from the end, since we know all the elements from the end to index are in sorted increasing order
        i = len(nums)-1
        while i > index and index != -1:
            if nums[i] > nums[index]:
                temp = nums[i]
                nums[i]=nums[index]
                nums[index] = temp
                break
            i-=1
    #after swaping we can reverse the elements before index, to get the next permutation,
    #edge case: if index is not found, still -1, that means that is the last permutation, so simply reversing gives the first permutation
        i= index+1
        j = len(nums)-1
        while i < j:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i+=1
            j-=1
        return nums
