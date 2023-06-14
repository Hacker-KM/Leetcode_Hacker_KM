# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        l = []
        while start:
            if start in l:
                return start
            else:
                l.append(start)
                start = start.next
        return None