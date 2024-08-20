https://leetcode.com/problems/kth-missing-positive-number/description/
#brute force
 def findKthPositive(self, arr: List[int], k: int) -> int:
        for i in range(len(arr)):
            if arr[i]<=k: #write and see the logic it correctly represnts the missing number
                k+=1
            else:
                break
        return k
