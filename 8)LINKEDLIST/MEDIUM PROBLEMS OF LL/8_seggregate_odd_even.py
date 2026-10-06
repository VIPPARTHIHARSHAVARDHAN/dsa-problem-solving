
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head):
        if head is None or head.next is None:
            return head
        
        odd=head
        even=head.next
        even_head=even
        while even and even.next:
            odd.next=even.next
            odd=odd.next
            
            even.next=odd.next
            even=even.next
        odd.next=even_head
            
        return head

# Object creation
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

# Connect nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Create Solution object
sol = Solution()

# Pass head to the method
result = sol.oddEvenList(node1)

# Print the linked list
current = result

while current:
    print(current.val, end=" ")
    current = current.next