class Node:
    def __init__(self,data,next=None,back=None):
        self.data = data
        self.next = next
        self.back = back

def convertArrToDLL(arr):
    head = Node(arr[0])
    prev = head
    for i in range(1,len(arr)):
        temp = Node(arr[i],None,prev)
        prev.next = temp
        prev = temp
    return head


def traveseDLL(head):
    temp=head
    dll = []
    while temp:
        dll.append(temp.data)
        temp=temp.next
    return dll

def delHeadDLL(head):
    if head==None or head.next ==None:
        return None
    prev = head
    head = head.next
    head.back = None
    prev.next = None
    return head

def delTailDLL(head):
    if head == None or head.next == None:
        return None
    temp = head
    while temp.next:
        temp=temp.next
    prev = temp.back
    prev.next = None
    temp.back = None
    return head


def delKElementDLL(head,k):
    if head == None:
        return None
    
    temp = head
    count=0
    while temp:
        count+=1
        if count==k:
            break
        temp=temp.next
    
    if temp:
        prev=temp.back
        front = temp.next
        if prev==None and front==None: # it is a single element node
            return None
        elif prev == None: # it is a head
            tempHead = temp
            head = temp.next
            head.back = None
            tempHead.next=None
            return head
        elif front == None: # it is a tail
            prev.next = None
            temp.back = None
            return head
        else:
            prev.next = front
            front.back = prev
            temp.next = None
            temp.back=None
            return head
    return head
            

def delNodeDLL(node):
    
    front = node.next
    prev = node.back

    # it is a tail
    if front == None:
        prev.next = None
        node.back = None
    else:
        prev.next = front
        front.back = prev
        node.next = None
        node.back = None

def insertHead(head,val):
    if head == None:
        return Node(val)
    
    newHead = Node(val,head)
    head.prev = newHead
    return newHead
    
def insertBeforeTail(head,val):
    if head == None or head.next == None:
        return insertHead(head,val)

    temp = head
    while temp.next:
        temp=temp.next
    prev = temp.back
    newNode = Node(val,temp,prev)
    prev.next = newNode
    temp.back = newNode
    return head
    
def insertBeforeKElelemnet(head,val,k):
    if k==1:
        return insertHead(head,val)

    temp= head
    count=0

    while temp:
        count+=1
        if count == k:
            break
        temp=temp.next
    
    if temp:
        prev = temp.back
        newNode = Node(val,temp,prev)
        prev.next = newNode
        temp.back = newNode

    return head

def insertBeforeNode(temp,val):
    prev = temp.back
    newNode = Node(val,temp,prev)
    prev.next = newNode
    temp.back=newNode


arr = [9,8,0,1,3]
head = convertArrToDLL(arr)
print(traveseDLL(head))

#del head
#head = delHeadDLL(head)

#del tail
#head = delTailDLL(head)

#del kth element
#head = delKElementDLL(head,4)

#del node
#delNodeDLL(head.next.next.next.next)

#inser head
#head = insertHead(head,2)

#insert before Tail
#head =insertBeforeTail(head,6)

#insert before Kth element
#head = insertBeforeKElelemnet(head,1,5)

#insert before new node
insertBeforeNode(head.next.next.next.next,2)

print(traveseDLL(head))
