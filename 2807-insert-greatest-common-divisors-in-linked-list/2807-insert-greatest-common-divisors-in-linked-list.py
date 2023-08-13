# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = head
        nextt = head.next
        while nextt!=None:
            new_node = ListNode(gcd(head.val,nextt.val))
            head.next = new_node
            new_node.next = nextt
            head = nextt
            nextt = nextt.next
        return new_head
