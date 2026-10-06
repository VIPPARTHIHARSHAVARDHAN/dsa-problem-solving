class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
node1=Node(2)
node2=Node(3)
node3=Node(4)
node4=Node(8)

node1.next=node2
node2.next=node3
node3.next=node4

head=node1
head=head.next
current=head
while current is not None:
    print(current.data,end=" ")
    current=current.next