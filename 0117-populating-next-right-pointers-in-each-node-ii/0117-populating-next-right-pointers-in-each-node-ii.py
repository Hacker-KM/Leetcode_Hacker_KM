"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def dfs(node,level):
            if node is None:
                return 
            if level in llist:
                llist[level].next = node
            llist[level] = node
            dfs(node.left,level+1)
            dfs(node.right,level+1)
        llist = {}
        dfs(root,0)
        return root