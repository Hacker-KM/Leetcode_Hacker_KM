# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        smaller = []
        larger = []
        for i in l:
            if i<x:
                smaller.append(i)
            else:
                larger.append(i)
        ans = smaller+larger
        if ans==[]:
            return 
        head = temp = ListNode(ans[0])
        for i in range(1,len(ans)):
            temp.next = ListNode(ans[i])
            temp = temp.next
        return head