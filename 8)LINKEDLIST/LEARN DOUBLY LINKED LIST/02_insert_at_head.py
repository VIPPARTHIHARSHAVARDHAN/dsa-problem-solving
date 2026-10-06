class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


# Create objects
node1 = Node(2)
node2 = Node(3)
node3 = Node(4)
node4 = Node(8)


# Connect the nodes
node1.next = node2

node2.prev = node1
node2.next = node3

node3.prev = node2
node3.next = node4

node4.prev = node3


# Head points to first node
head = node1
new_node=Node(1)
new_node.next=head
head.prev=new_node
head=new_node


# Traversal
current = head

while current is not None:
    print(current.data, end=" ")
    current = current.next