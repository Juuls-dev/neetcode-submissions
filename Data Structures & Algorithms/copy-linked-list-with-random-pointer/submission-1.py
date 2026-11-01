"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        copies ={}
        p = head

        while p:
            copies[p]= Node(p.val)
            p = p.next

        cur = head 
        while cur:
            copies[cur].next = copies.get(cur.next)
            copies[cur].random = copies.get(cur.random)
            cur = cur.next
        return copies[head]
