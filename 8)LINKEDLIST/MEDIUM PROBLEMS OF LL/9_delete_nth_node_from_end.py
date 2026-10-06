#brute force solution
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nthnode(self, head,n):
        length = 0
        current = head

        while current:
            length += 1
            current = current.next

        if n < 1 or n > length:
            return head

        if n == length:
            return head.next

        steps = length - n - 1
        current = head

        while steps > 0:
            current = current.next
            steps -= 1

        current.next = current.next.next
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
result = sol.nthnode(node1,2)

# Print the linked list
current = result

while current:
    print(current.val, end=" ")
    current = current.next
    
    
    
#optimal solution
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nthnode(self, head,n):
        if head is None or n < 1:
            return head

        fast = head

        # Move fast n steps ahead
        for i in range(n):
            if fast is None:
                return head  # n is larger than the list length
            fast = fast.next

        # If fast is None, remove the head
        if fast is None:
            return head.next

        slow = head

        # Move both pointers until fast reaches the last node
        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        # Remove the node after slow
        slow.next = slow.next.next
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
result = sol.nthnode(node1,2)

# Print the linked list
current = result

while current:
    print(current.val, end=" ")
    current = current.next
    
    


