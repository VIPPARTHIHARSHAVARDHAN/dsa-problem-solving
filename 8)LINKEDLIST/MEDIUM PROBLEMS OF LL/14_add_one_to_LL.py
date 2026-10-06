#brute force
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
    def addone(self,head):
        head=self.reverseList(head)
        temp=head
        carry=1
        while temp:
            temp.val=temp.val+carry
            if temp.val<10:
                carry=0
                break
            else:
                carry=1
                temp.val=0
            temp=temp.next
        if carry==1:
            new_node=ListNode(1)
            head=self.reverseList(head)
            new_node.next=head
            head=new_node
            return head
        head=self.reverseList(head)
    
        return head
        
        


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
result = solution.addone(head)

# Print reversed linked list
current = result

while current is not None:
    print(current.val, end=" ")
    current = current.next
        



#optimal solution

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addOne(self, head):

        def add_carry(node):
            if node is None:
                return 1

            carry = add_carry(node.next)

            if carry == 0:
                return 0

            node.val = node.val + carry

            if node.val < 10:
                return 0
            else:
                node.val = 0
                return 1

        carry = add_carry(head)

        if carry == 1:
            new_node = ListNode(1)
            new_node.next = head
            head = new_node

        return head


# Object creation: 1 -> 2 -> 9
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(9)

obj = Solution()
head = obj.addOne(head)

temp = head
while temp is not None:
    print(temp.val, end=" ")
    temp = temp.next