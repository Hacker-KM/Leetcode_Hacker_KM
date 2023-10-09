# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        top = 0 
        left = 0
        bottom = m-1
        right = n-1
        ans = [[-1 for _ in range(n)] for _ in range(m)]
        while left<=right and top<=bottom:
            for i in range(left,right+1):
                if head:
                    ans[top][i] = head.val
                    head = head.next
            top+=1
            for i in range(top,bottom+1):
                if head:
                    ans[i][right] = head.val
                    head = head.next
            right-=1
            if top <=bottom:
                for i in range(right,left-1,-1):
                    if head:
                        ans[bottom][i] = head.val
                        head = head.next
                bottom-=1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    if head:
                        ans[i][left] = head.val
                        head = head.next
                left+=1
        return ans