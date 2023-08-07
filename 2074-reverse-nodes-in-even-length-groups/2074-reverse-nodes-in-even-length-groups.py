# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        ans = []
        while head:
            l.append(head.val)
            head = head.next
        right = 1
        left = 0
        while left+right<=len(l):
            temp = l[left:left+right]
            if len(temp)%2==0:
                temp = temp[::-1]
                ans+= temp
            else:
                ans+= temp
            left+=right
            right+=1
        remain = len(l)-len(ans)
        temp2=[]
        if remain%2==0:
            for i in range(-remain,0,1):
                temp2.append(l[i])
            ans+=temp2[::-1]
        else:    
            for i in range(-remain,0,1):
                ans.append(l[i])
        head=temp=ListNode(ans[0])
        for i in range(1,len(ans)):
            temp.next = ListNode(ans[i])
            temp = temp.next
        return head


        