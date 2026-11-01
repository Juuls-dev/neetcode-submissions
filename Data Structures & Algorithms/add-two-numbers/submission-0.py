# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        mock = ListNode()
        tail = mock
        k=0

        while l1 or l2 or k:
            x1 = l1.val if l1 else 0
            x2 = l2.val if l2 else 0
            total = x1 + x2 + k
            k, cur = total // 10 , total % 10
            tail.next = ListNode(cur)
            tail = tail.next

            l1 = l1.next if l1 else None
            l2  = l2.next if l2 else None

        return mock.next


        