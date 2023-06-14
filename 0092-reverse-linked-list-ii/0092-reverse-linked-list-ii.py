# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        p = l[0:left-1] + l[left-1:right][::-1]+l[right:len(l)]
        cur = dummy = ListNode(0)
        for e in p:
            cur.next = ListNode(e)
            cur = cur.next
        return dummy.next
        