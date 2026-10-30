# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow=ListNode(0)
        p = slow
        slow.next =head

        fast = head
        i = 0
        for _ in range(n):
            fast =fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        
        return p.next

        