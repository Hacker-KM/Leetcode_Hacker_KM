# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        p=[]
        for i in l:
            if l.count(i)==1:
                p.append(i)
        if p==[]:
            return 
        head = temp = ListNode(p[0])
        for i in range(1,len(p)):
            temp.next = ListNode(p[i])
            temp = temp.next
        return head