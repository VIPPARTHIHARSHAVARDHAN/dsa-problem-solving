class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Solution:
    def middleNode(self, head):

        # Find length
        count = 0
        temp = head

        while temp:
            count += 1
            temp = temp.next

        # Find middle position
        middle = count // 2

        # Move to middle node
        temp = head

        while middle > 0:
            temp = temp.next
            middle -= 1

        return temp.data


# Creating objects
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

# Connecting objects
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Head
head = node1

# Create Solution object
obj = Solution()

# Find middle
answer = obj.middleNode(head)

print(answer)




#optimal solution TortoiseHare Method
slow = head
fast = head

while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next

return slow