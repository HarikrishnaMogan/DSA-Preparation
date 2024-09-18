https://leetcode.com/problems/odd-even-linked-list/
#my solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        temp =head
        prev = None
        evenHead = head.next
        c=1
        while temp.next:
            next = temp.next
            temp.next = temp.next.next
            prev = temp
            temp = next
            c+=1
        
        if c%2==0:
            prev.next = evenHead
        else:
            temp.next = evenHead
        return head
#......................................................
#strivers solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        odd = head
        even = head.next
        evenHead = head.next
        while even != None and even.next != None:
            odd.next = odd.next.next
            even.next = even.next.next

            odd = odd.next
            even = even.next
        
        #attach the odd tail to evenHead
        odd.next = evenHead

        return head

        
