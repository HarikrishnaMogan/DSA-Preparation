https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        for i in range(n):
            fast=fast.next
        
        if fast == None:
            newHead = head.next
            head.next = None
            return newHead
        
        
        while fast.next != None:
            fast = fast.next
            slow=slow.next

        delNode = slow.next
        slow.next = slow.next.next
        delNode.next = None
        return head
