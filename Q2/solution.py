# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node
        dummy = ListNode(0)
        dummy.next = head
        # Create two pointers
        first = dummy
        second = dummy
        # Advance first pointer by n+1 steps
        for i in range(n+1):
            first = first.next
        # Advance both pointers until first reaches the end
        while first:
            first = first.next
            second = second.next
        # Remove the nth node
        second.next = second.next.next
        return dummy.next

# Definition for checking solution

# if __name__ == '__main__':
#     # Create a linked list
#     head = ListNode(1)
#     head.next = ListNode(2)
#     head.next.next = ListNode(3)
#     head.next.next.next = ListNode(4)
#     head.next.next.next.next = ListNode(5)
#     # Create a solution object
#     obj = Solution()
#     # Remove the nth node
#     head = obj.removeNthFromEnd(head, 2)
#     # Print the linked list
#     while head:
#         print(head.val)
#         head = head.next

        
