
https://leetcode.com/problems/rotate-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def findKthElement(node,k):
            temp = node
            c=0
            while temp:
                c+=1
                if c==k:
                    return temp
                temp = temp.next
            

        tail = head
        len = 1
        while tail and tail.next != None:
            len+=1
            tail=tail.next
        
        if k%len == 0:
            return head
      

        tail.next = head
        k = k%len
        k = len-k
        #find kth element
        newLast = findKthElement(head,k)
        head = newLast.next
        newLast.next = None
        return head
