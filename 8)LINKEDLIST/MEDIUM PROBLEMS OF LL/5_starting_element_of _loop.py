#brute force solution
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head):
        visited = set()
        current = head
        while current is not None:
            if current in visited:
                return current.val
            visited.add(current)
            current=current.next
        return None
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2
sol = Solution()
print(sol.hasCycle(node1))



#optimal solution TortoiseHare Method

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head):
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                slow=head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
                
        return None     
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2
sol = Solution()
result=sol.hasCycle(node1)
if result is not None:
    print(result.val)
else:
    print(None)
