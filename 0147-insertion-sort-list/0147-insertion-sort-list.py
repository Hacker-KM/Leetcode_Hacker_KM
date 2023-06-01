# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums=[]
        temp = head
        while temp:
            nums.append(temp.val)
            temp = temp.next
        for i in range(len(nums)):
            j = i
            while j > 0 and nums[j - 1] > nums[j]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
                j = j - 1
        k =0
        r=head
        while r:
            r.val=nums[k]
            k=k+1
            r=r.next
        return head
        
    

        
