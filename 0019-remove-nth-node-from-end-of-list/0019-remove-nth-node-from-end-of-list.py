# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        actual = head
        l =0 
        while actual:
            actual = actual.next
            l+=1
        actual = head
        step= l-n
        if step==0:
            head = head.next
        else:
            s=1
            while s<step:
                actual=actual.next
                s+=1
            actual.next = actual.next.next
        return head