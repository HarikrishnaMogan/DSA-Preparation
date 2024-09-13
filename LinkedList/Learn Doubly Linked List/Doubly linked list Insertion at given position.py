https://www.geeksforgeeks.org/problems/insert-a-node-in-doubly-linked-list/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=insert-a-node-in-doubly-linked-list

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

'''
#Function to insert a new node at given position in doubly linked list.
def addNode(head, p, data):
    # Code here
    temp = head
    c=0
    while temp:
        if c==p:
            break
        temp=temp.next
        c+=1
        
    newNode = Node(data)
    newNode.next = temp.next
    newNode.prev = temp
    temp.next = newNode
    return head
