#create a template for ll
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


arr=[23,4,5,7]
#arr to LL 
head = convertArrToLL(arr)
print(head.data)

#travesing LL
print(TraverseLL(head))

#len of ll
print(getLenLL(head))

#check ele exists
print(checkElementLL(head, 5))
