  
class Node:
    def __init__(self,val, next=None):
        self.val = val
        self.next = next


class Solution:
    def delmiddleNode(self, head):
        if head is None:
            return None

        temp=head
        count0=0
        count1=0
        count2=0
        while temp:
            if temp.val==0:
                count0+=1
            elif temp.val==1:
                count1+=1
            else:
                count2+=1
            temp=temp.next
        temp=head
        for i in range(count0):
            temp.val=0
            temp=temp.next
        for j in range(count1):
            temp.val=1
            temp=temp.next
        for k in range(count2):
            temp.val=2
            temp=temp.next      
        return head

# Create nodes
node1 = Node(1)
node2 = Node(0)
node3 = Node(2)
node4 = Node(0)
node5 = Node(1)

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
    print(temp.val, end=" ")
    temp=temp.next
    
    
    
#optimal solution 
  
class Node:
    def __init__(self,val, next=None):
        self.val = val
        self.next = next


class Solution:
    def delmiddleNode(self, head):
        if head is None:
            return None

        # Create dummy nodes
        l0 = Node(-1)
        l1 = Node(-1)
        l2 = Node(-1)

        # Tail pointers
        tail0 = l0
        tail1 = l1
        tail2 = l2

        temp = head

        # Separate nodes into three lists
        while temp:
            next_node = temp.next

            # Detach current node
            temp.next = None

            if temp.val == 0:
                tail0.next = temp
                tail0 = temp

            elif temp.val == 1:
                tail1.next = temp
                tail1 = temp

            else:
                tail2.next = temp
                tail2 = temp

            temp = next_node

        # Connect the three lists
        tail0.next = l1.next if l1.next else l2.next
        tail1.next = l2.next

        # Return the first non-empty list
        if l0.next:
            return l0.next
        elif l1.next:
            return l1.next
        else:
            return l2.next
# Create nodes
node1 = Node(1)
node2 = Node(0)
node3 = Node(2)
node4 = Node(0)
node5 = Node(1)

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
    print(temp.val, end=" ")
    temp=temp.next
    
 
