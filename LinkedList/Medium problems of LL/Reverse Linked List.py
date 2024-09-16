https://leetcode.com/problems/reverse-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next==None:
            return head
        prev = None
        current = head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev

#..........................................................
#recurive solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            if head== None or head.next == None:
                return head
            
            newHead = reverse(head.next)
            front = head.next
            front.next = head
            head.next = None
            return newHead
        return reverse(head)
