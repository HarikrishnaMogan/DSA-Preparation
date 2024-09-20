https://www.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=given-a-linked-list-of-0s-1s-and-2s-sort-it

#User function Template for python3
'''
	Your task is to segregate the list of 
	0s,1s and 2s.
	
	Function Arguments: head of the original list.
	Return Type: head of the new list formed.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''
class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        #code here
        
        zeroHead = Node(-1)
        oneHead = Node(-1)
        twoHead = Node(-1)
        
        zero = zeroHead
        one = oneHead
        two = twoHead
        
        
        temp = head
        
        while temp:
            if temp.data == 0:
                zero.next = temp
                zero = temp
            elif temp.data ==1:
                one.next = temp
                one = temp
            else:
                two.next = temp
                two = temp
            temp = temp.next
        
        if oneHead.next:
            zero.next = oneHead.next
        else:
            zero.next = twoHead.next
        
        one.next = twoHead.next
        two.next = None
        return zeroHead.next
