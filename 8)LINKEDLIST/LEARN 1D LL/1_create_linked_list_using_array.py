class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


arr = [2, 5, 8, 7]

# Create first node
head = Node(arr[0])

# Current node
current = head

# Link remaining elements
for i in range(1, len(arr)):
    new_node = Node(arr[i])
    current.next = new_node
    current = current.next


# Print the linked list
current = head

while current is not None:
    print(current.data, end=" ")
    current = current.next