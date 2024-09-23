https://leetcode.com/problems/reverse-nodes-in-k-group/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverseLL(node):
            tem = node
            prev = None
            while tem !=None:
                next = tem.next
                tem.next = prev
                prev = tem
                tem=next
            
        
        def kthEle(node, c):
            tem = node
            c-=1
            while tem !=None and c > 0:
                c-=1
                tem=tem.next
            return tem
        
        temp = head
        prevLast = None
        nextNode = None
        while temp !=None:

            kNode = kthEle(temp,k)
            
            if kNode == None:
                if prevLast:
                    prevLast.next = temp
                break
            
            nextNode = kNode.next
            kNode.next = None
            reverseLL(temp)

            if temp == head:
                head =kNode
            else:
                prevLast.next = kNode

            prevLast = temp
            temp = nextNode

        return head
        
