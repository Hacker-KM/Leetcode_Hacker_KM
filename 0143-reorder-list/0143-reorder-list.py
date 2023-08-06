# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        l = []
        temp = head
        while temp:
            l.append(temp)
            temp = temp.next
        left = 0
        right = len(l)-1
        while left<right:
            l[left].next = l[right]
            left+=1
            if left==right:
                break
            l[right].next = l[left]
            right-=1
        l[right].next = None