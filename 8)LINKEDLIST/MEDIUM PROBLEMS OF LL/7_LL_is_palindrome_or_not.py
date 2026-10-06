class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head):
        current=head
        stack=[]
        while current is not None:
            stack.append(current.val)
            current=current.next
        current=head
        while stack:
            element=stack.pop()
            if current.val != element:
                return False
            current=current.next
        return True
# Object creation
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(2)
node4 = ListNode(1)

# Connecting nodes
node1.next = node2
node2.next = node3
node3.next = node4

# Create Solution object
sol = Solution()

# Pass the head node to the method
print(sol.isPalindrome(node1))






#optimal solution using middle + reverse

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True

        fast=head
        slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        current=slow
        while current is not None:
            new_node=current.next
            current.next=prev
            prev=current
            current=new_node
        first=head
        second=prev
        while second:
            if first.val!=second.val:
                return False
            first=first.next
            second=second.next
        return True

# Object creation
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(2)
node4 = ListNode(1)

# Connect nodes
node1.next = node2
node2.next = node3
node3.next = node4

# Create Solution object
sol = Solution()

# Pass head to the method
print(sol.isPalindrome(node1))

