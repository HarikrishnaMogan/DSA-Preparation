
https://leetcode.com/problems/copy-list-with-random-pointer/description/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:

    #insert copyNode in between
    def insertCopyNode(self,head):
        temp=head
        while temp != None:
            copyNode = Node(temp.val)
            copyNode.next = temp.next
            temp.next = copyNode
            temp = temp.next.next
    
    #connect random pointer
    def connectRandomPointer(self,head):
        temp = head
        while temp != None:
            copyNode = temp.next
            if temp.random != None:
                copyNode.random = temp.random.next
            else:
                copyNode.random = None
            temp = temp.next.next
    
    #get copy node and revert input LL
    def getCopyNode(self, head):
        temp = head
        dummy = Node(-1)
        res = dummy
        while temp != None:
            res.next = temp.next
            temp.next = temp.next.next
            temp = temp.next
            res = res.next
        copyHead = dummy.next
        dummy.next = None
        return copyHead




    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        self.insertCopyNode(head)
        self.connectRandomPointer(head)
        return self.getCopyNode(head)
