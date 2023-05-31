class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans= []
        for i in nums1:
            if i==nums2[-1]:
                ans.append(-1)
            k = nums2.index(i)
            l = nums2[k:len(nums2)]
            for j in range(len(l)):
                if l[j]>i:
                    ans.append(l[j])
                    break
                elif j==len(l)-1 and l[j]<i:
                    ans.append(-1)
            
        return ans
        

            