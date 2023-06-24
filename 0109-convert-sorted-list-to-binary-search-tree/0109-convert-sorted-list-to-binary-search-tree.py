# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head):
        A = []
        temp = head
        while temp:
            A.append(temp.val)
            temp = temp.next
        def make(i,j):
            if i<=j:
                m = (i+j)//2
                n = TreeNode(A[m])
                n.left = make(i,m-1)
                n.right = make(m+1,j)
                return n
        return make(0, len(A)-1)