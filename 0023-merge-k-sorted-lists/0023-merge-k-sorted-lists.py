# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values= []
        head = None
        for l in lists:
            while l:
                values.append(l.val)
                l = l.next
                
        values.sort()
        
        while values:
            if head == None:
                head = ListNode(values.pop(0))
                pointer = head
            else:
                pointer.next = ListNode(values.pop(0))
                pointer = pointer.next
        
        return head
