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
        oldTCopy={None:None}
        cur = head
        while cur:
            copy=Node(cur.val)
            oldTCopy[cur]=copy
            cur=cur.next
        cur=head
        while cur:
            copy=oldTCopy[cur]
            copy.next=oldTCopy[cur.next]
            copy.random= oldTCopy[cur.random]
            cur=cur.next
        return oldTCopy[head]
        