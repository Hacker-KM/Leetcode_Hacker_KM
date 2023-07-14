# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        l1=[]
        for i in range(len(l)):
            if l[i]==0:
                l1.append(i)
        ans = []
        for i in range(len(l1)-1):
            ans.append(sum(l[l1[i]:l1[i+1]]))
        if ans != []:
            new_head = ListNode(ans[0])
            curr_node = new_head
            for i in range(1, len(ans)):
                curr_node.next = ListNode(ans[i])
                curr_node = curr_node.next
            return new_head
        return None




        
