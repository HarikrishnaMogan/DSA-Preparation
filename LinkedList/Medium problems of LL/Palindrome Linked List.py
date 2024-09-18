https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def reverseLL(head):
            if head == None or head.next == None:
                return head
            
            prev =None
            temp = head
            while temp:
                next = temp.next
                temp.next = prev
                prev = temp
                temp = next
            return prev

        #find the mid
        slow = head
        fast =head
        while fast.next != None and fast.next.next !=None:
            slow = slow.next
            fast = fast.next.next
        #reverse the other half
        newHead = reverseLL(slow.next)
        #compare both half
        second = newHead
        first = head
        while second:
            if first.val != second.val:
                reverseLL(newHead) #convert the LL back to actual
                return False
            first=first.next
            second = second.next
        reverseLL(newHead) #convert the LL back to actual
        return True
