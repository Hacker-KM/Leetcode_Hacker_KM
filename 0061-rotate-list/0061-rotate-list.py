# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return 
        l = []
        
        while head:
            l.append(head.val)
            head = head.next
        while k%len(l)>0:
            p = l[-1]
            l.insert(0, p)
            l.pop()
            k-=1
        cur = dummy = ListNode(0)
        for e in l:
            cur.next = ListNode(e)
            cur = cur.next
        return dummy.next

            