class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# Create nodes
node1 = Node(2)
node2 = Node(5)
node3 = Node(8)
node4 = Node(7)


# Link nodes
node1.next = node2
node2.next = node3
node3.next = node4


# Head points to first node
head = node1


# Element to search
target = 8


# Search
current = head

while current is not None:

    if current.data == target:
        print("Element found")
        break

    current = current.next

else:  
    print("Element not found")