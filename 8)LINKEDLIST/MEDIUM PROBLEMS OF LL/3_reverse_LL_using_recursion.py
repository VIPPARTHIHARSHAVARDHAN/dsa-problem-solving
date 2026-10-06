class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):

        if head is None or head.next is None:
            return head

        new_head = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return new_head


# Create nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

# Connect nodes
node1.next = node2
node2.next = node3
node3.next = node4

# Head
head = node1

# Create Solution object
solution = Solution()

# Reverse
result = solution.reverseList(head)

# Print
current = result

while current is not None:
    print(current.val, end=" ")
    current = current.next