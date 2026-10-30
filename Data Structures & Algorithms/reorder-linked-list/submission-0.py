# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow  = fast = head
        p1= head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        p2= slow.next
        slow.next = None
        prev= None

        while p2:
            n_node = p2.next
            p2.next =prev
            prev = p2
            p2 = n_node
        p2 = prev 

        while p2:
            n_p1 = p1.next
            n_p2 = p2.next

            p1.next = p2
            p2.next = n_p1

            p1 = n_p1
            p2 = n_p2


