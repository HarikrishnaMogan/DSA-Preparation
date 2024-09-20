https://leetcode.com/problems/intersection-of-two-linked-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        t1 = headA
        t2=headB
        while t1 != t2: #if first node equals return that node
            t1=t1.next
            t2=t2.next
            if t1==t2: #this will return intersection node or return null if there is no intersection because at some point if no intersection both t1 and t2 become null
                return t1
            
            if t1==None:
                t1=headB
            if t2==None:
                t2=headA
        return t1
