
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, head1, head2):

        visited = {}

        temp = head1

        while temp:
            visited[temp] = 1
            temp = temp.next

        temp = head2

        while temp:
            if temp in visited:
                return temp

            temp = temp.next

        return None


# Create common nodes
node3 = Node(30)
node4 = Node(40)

node3.next = node4


# Create nodes for List 1
node1 = Node(10)
node2 = Node(20)

node1.next = node2
node2.next = node3


# Create nodes for List 2
node5 = Node(5)
node6 = Node(15)

node5.next = node6
node6.next = node3

obj = Solution()

result = obj.getIntersectionNode(node1, node5)
if result:
    print("Intersection node:", result.val)
else:
    print("No intersection")
    
    
    
#optimal solution
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, head1, head2):
        temp1=head1
        temp2=head2
        while temp1 is not temp2:
            if temp1 is None:
                temp1=head2
            else:
                temp1=temp1.next
            if temp2 is None:
                temp2=head1
            else:
                temp2=temp2.next
        return temp1
        
# Create common nodes
node3 = Node(30)
node4 = Node(40)

node3.next = node4


# Create nodes for List 1
node1 = Node(10)
node2 = Node(20)

node1.next = node2
node2.next = node3


# Create nodes for List 2
node5 = Node(5)
node6 = Node(15)

node5.next = node6
node6.next = node3

obj = Solution()

result = obj.getIntersectionNode(node1, node5)
if result:
    print("Intersection node:", result.val)
else:
    print("No intersection")
