class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Solution:
    def delmiddleNode(self, head):
        if head is None or head.next is None:
            return None

        # 1. Find the length
        count = 0
        temp = head

        while temp:
            count += 1
            temp = temp.next

        # 2. Find the middle index (0-based)
        middle = count // 2

        # 3. Move to the node before the middle
        temp = head
        for _ in range(middle - 1):
            temp = temp.next

        # 4. Delete the middle node
        temp.next = temp.next.next

        return head


# Create nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

# Connect nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Call the method
obj = Solution()
result = obj.delmiddleNode(node1)

# Print the result
temp = result
while temp is not None:
    print(temp.data, end=" ")
    temp=temp.next
    
  
  
  
  
  #optimal solution using tortoise hare  
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Solution:
    def delmiddleNode(self, head):
        if head is None or head.next is None:
            return None

        slow = head
        fast=head
        prev=None
        while fast.next and fast:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=slow.next
        return head


# Create nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

# Connect nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Call the method
obj = Solution()
result = obj.delmiddleNode(node1)

# Print the result
temp = result
while temp is not None:
    print(temp.data, end=" ")
    temp=temp.next