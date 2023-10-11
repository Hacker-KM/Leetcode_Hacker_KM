# class Node:
#     def __init__(self, val, prev=None, next=None, child=None):
#         self.val = val
#         self.prev = prev
#         self.next = next
#         self.child = child

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        def dfs(node):
            current = node
            last_node = None
            
            while current:
                if current.child:
                    next_node = current.next
                    child_head, child_tail = dfs(current.child)
                    current.next = child_head
                    child_head.prev = current
                    current.child = None
                    
                    if next_node:
                        child_tail.next = next_node
                        next_node.prev = child_tail
                    
                    last_node = child_tail
                else:
                    last_node = current
                
                current = current.next
            
            return node, last_node
        head,curr = dfs(head)
        return head
