
https://www.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=add-1-to-a-number-represented-as-linked-list
   
        def helper(node):
            
            if node == None:
                return 1
            carry = helper(node.next)
            node.data = node.data+carry
            if node.data < 10:
                return 0
            node.data = 0
            return 1
            
            
        
        temp = head
        carry = helper(temp)
        if carry == 1:
            newNode = Node(1)
            newNode.next = temp
            return newNode
        else:
            return head
#............................................................................

# without recusrssion

'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def addOne(self,head):
        #Returns new head of linked List.
        
        def reverse(node):
            temp = node
            prev = None
            while temp:
                next = temp.next
                temp.next = prev
                prev = temp
                temp = next
            return prev
        
        tempHead = reverse(head)
        carry = 1
        temp = tempHead
        while temp:
            temp.data = temp.data+carry
            if temp.data < 10:
                carry =0
                break
            else:
                temp.data = 0
                carry =1
            temp=temp.next
        head = reverse(tempHead)
        if carry == 1:
            newNode = Node(1)
            newNode.next = head
            return newNode
        
        return head
