https://www.geeksforgeeks.org/problems/max-sum-in-sub-arrays0824/0?category&utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=max-sum-in-sub-arrays

def pairWithMaxSum(self, arr):
        # Your code goes here
        maxi = 0
        for i in range(len(arr)-1):
            sum = arr[i]+arr[i+1]
            maxi = max(maxi, sum)
        return maxi



# Example:
# Input : arr[] = [4, 3, 1, 5, 6]
# Output : 11
# Explanation : Subarrays with smallest and second smallest are:- [4, 3] smallest = 3,second smallest = 4
# [4, 3, 1] smallest = 1, second smallest = 3
# [4, 3, 1, 5] smallest = 1, second smallest = 3
# [4, 3, 1, 5, 6] smallest = 1, second smallest = 3
# [3, 1] smallest = 1, second smallest = 3
# [3, 1, 5] smallest = 1, second smallest = 3
# [3, 1, 5, 6] smallest = 1, second smallest = 3
# [1, 5] smallest = 1, second smallest = 5
# [1, 5, 6] smallest = 1, second smallest = 5
# [5, 6] smallest = 5, second smallest = 6
# Maximum sum among all above choices is, 5 + 6 = 11.
