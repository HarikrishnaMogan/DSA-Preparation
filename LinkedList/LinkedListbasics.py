
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next



def convertArrToLL(arr):
    head = Node(arr[0])
    mover = head
    for i in range(1,len(arr)):
        temp = Node(arr[i])
        mover.next = temp
        mover = temp
    return head

def TraverseLL(head):
    ll = []
    temp = head
    while temp:
        ll.append(temp.data)
        temp=temp.next
    return ll

def getLenLL(head):
    temp = head
    cnt=0
    while temp:
        cnt+=1
        temp=temp.next
    return cnt

def checkElementLL(head,val):
    temp = head
    while temp:
        if temp.data == val:
            return True
        temp = temp.next
    return False

#deletion....................
def delHead(head):
    if head==None:
        return head
    head = head.next
    return head

def delTail(head):
    if head == None or head.next==None:
        return None
    temp = head
    while temp.next.next != None:
        temp=temp.next
    temp.next = None
    return head

def delEleAtPos(head, k):
    if head==None:
        return head
    if k==1:
        head=head.next
        return head
    temp=head
    prev=None
    count=0
    while temp:
        count+=1
        if count==k:
            prev.next = prev.next.next
            break
        prev=temp
        temp=temp.next
    return head

def delEleAtLL(head, ele):
    if head==None:
        return head
    if head.data==ele:
        head = head.next
        return head
    temp=head
    prev=None
    while temp:
        if temp.data == ele:
            prev.next = prev.next.next
            break
        prev=temp
        temp=temp.next
    return head

#...................


#Insertion >>>>>>>>>>>>>>>>>>>>>>>>

def insertHead(head,val):
    if head == None:
        return Node(val)
    return Node(val,head)

def inserTail(head,val):
    if head == None:
        return Node(val)
    temp = head
    while temp.next:
        temp=temp.next
    temp.next = Node(val)
    return head

def insertAtPos(head,val,k):
    if head==None:
        if k==1:
            return Node(val)
    if k==1:
        temp = Node(val,head)
        return temp
    temp = head
    count=0
    while temp:
        count+=1
        if count == k-1:
            x = Node(val,temp.next)
            temp.next = x
            break
        temp=temp.next
    return head

def insertBeforeEle(head,val,ele):
    if head == None:
        return head
    if head.data==ele:
        return Node(val,head)
    temp = head
    while temp:
        if temp.next != None and temp.next.data == ele:
            x=Node(val,temp.next)
            temp.next=x
            break
        temp=temp.next
    return head


arr=[23,4,5,7,8]
#arr to LL 
head = convertArrToLL(arr)
print(head.data)

# #travesing LL
# print(TraverseLL(head))

# #len of ll
# print(getLenLL(head))

# #check ele exists
# print(checkElementLL(head, 5))

#del head
# head = delHead(head)
# print(TraverseLL(head))

#del Tail
# head = delTail(head)
# print(TraverseLL(head))

#del ele at pos
# head=delEleAtPos(head,2)
# print(TraverseLL(head))

#del ele at LL
# head=delEleAtLL(head,4)
# print(TraverseLL(head))

#insert head
# head = insertHead(head,3)
# print(TraverseLL(head))

#insert Tail
# head = inserTail(head,10)
# print(TraverseLL(head))

#insert at pos
# head = insertAtPos(head,10,1)
# print(TraverseLL(head))

#insert before ele
head = insertBeforeEle(head,10,5)
print(TraverseLL(head))
