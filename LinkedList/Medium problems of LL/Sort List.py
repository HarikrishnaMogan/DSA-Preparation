
https://leetcode.com/problems/sort-list/description/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def findMiddle(node):
            slow = node
            fast=node.next
            while fast != None and fast.next != None:
                slow=slow.next
                fast=fast.next.next
            return slow
        
        def mergeSort(head):
            if head == None or head.next == None:
                return head
            
            middle = findMiddle(head)
            rightHead = middle.next
            middle.next = None
            leftHead = mergeSort(head)
            rightHead = mergeSort(rightHead)
            return merge(leftHead,rightHead)
        
        def merge(left,right):
            dummyNode = ListNode(-1)
            temp = dummyNode
            while left != None and right != None:
                if left.val < right.val:
                    temp.next = left
                    left = left.next
                else:
                    temp.next = right
                    right = right.next 
                temp = temp.next
            
            if left != None:
                temp.next = left
            if right != None:
                temp.next = right
            return dummyNode.next


        return  mergeSort(head)
