class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        current = head
        while current:
            if current.child:
                next_node = current.next
                child_head = current.child
                while child_head.next:
                    child_head = child_head.next
                current.next = current.child
                current.child.prev = current
                current.child = None
                child_head.next = next_node
                if next_node:
                    next_node.prev = child_head
            current = current.next
        return head
