#brute force solution
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head):
        visited = {}
        current = head
        position=0

        while current is not None:
            if current in visited:
                return position - visited[current]
            visited[current]=position
            position+=1
            current = current.next

        return 0
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
                count=1
                slow=slow.next
                while slow!=fast:
                    count+=1
                    slow=slow.next
                return count
                                
               
                
        return 0  
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


 

