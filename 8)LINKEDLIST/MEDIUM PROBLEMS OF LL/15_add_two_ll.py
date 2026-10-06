class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy
        carry = 0

        while l1 is not None or l2 is not None or carry:
            total = carry

            if l1 is not None:
                total += l1.val
                l1 = l1.next

            if l2 is not None:
                total += l2.val
                l2 = l2.next

            carry = total // 10
            digit = total % 10

            tail.next = ListNode(digit)
            tail = tail.next

        return dummy.next


# Object creation:
# 342 is stored as 2 -> 4 -> 3
l1 = ListNode(2, ListNode(4, ListNode(3)))

# 465 is stored as 5 -> 6 -> 4
l2 = ListNode(5, ListNode(6, ListNode(4)))

obj = Solution()
result = obj.addTwoNumbers(l1, l2)

# Print result
temp = result
while temp is not None:
    print(temp.val, end=" ")
    temp = temp.next