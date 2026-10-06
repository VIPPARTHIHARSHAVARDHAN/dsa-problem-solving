class Solution(object):

    class ListNode(object):
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

    def reverseList(self, head):
        if head is None:
            return None

        stack = []
        current = head

        # Put all nodes into stack
        while current is not None:
            stack.append(current)
            current = current.next

        # Last node becomes head
        head = stack.pop()
        current = head

        # Connect nodes in reverse order
        while stack:
            node = stack.pop()
            current.next = node
            current = current.next

        current.next = None

        return head


# Object creation
node1 = Solution.ListNode(1)
node2 = Solution.ListNode(2)
node3 = Solution.ListNode(3)
node4 = Solution.ListNode(4)

# Connect nodes
node1.next = node2
node2.next = node3
node3.next = node4

# Create Solution object
solution = Solution()

# Reverse
result = solution.reverseList(node1)

# Print
current = result

while current:
    print(current.val, end=" ")
    current = current.next
   
    
#optimal
# Node class
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def reverseList(self, head):

        current = head
        prev = None

        while current is not None:

            new_node = current.next
            current.next = prev
            prev = current
            current = new_node

        return prev


# -------------------------
# Object creation
# -------------------------

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

# Connecting nodes
node1.next = node2
node2.next = node3
node3.next = node4

# Head of linked list
head = node1

# Create Solution object
solution = Solution()

# Reverse linked list
result = solution.reverseList(head)

# Print reversed linked list
current = result

while current is not None:
    print(current.val, end=" ")
    current = current.next
        

