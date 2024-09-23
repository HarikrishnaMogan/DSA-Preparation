https://www.geeksforgeeks.org/problems/find-pairs-with-given-sum-in-doubly-linked-list/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=find-pairs-with-given-sum-in-doubly-linked-list

class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        # code here
        
        def findTail(node):
            temp = node
            while temp.next:
                temp=temp.next
            return temp
        
        left = head
        right = findTail(head)
        ans = []
        
        while left.data < right.data:
            sum = left.data+right.data
            if sum == target:
                ans.append([left.data,right.data])
                left=left.next
                right=right.prev
            elif sum < target:
                left=left.next
            else:
                right=right.prev
        return ans
