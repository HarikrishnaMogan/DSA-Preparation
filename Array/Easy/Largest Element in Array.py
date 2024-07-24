https://www.geeksforgeeks.org/problems/largest-element-in-array4009/0?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=largest-element-in-array

class Solution:
    def largest(self, n : int, arr : List[int]) -> int:
        # code here
        max = arr[0]
        for i in range(n):
            if arr[i] > max:
                max = arr[i]
        return max
