class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = []
        l = []
        ans = []
        for i in list1:
            if i in list2:
                k = list1.index(i)+list2.index(i)
                l.append(k)
                o = [k,i]
                d.append(o)
        p = min(l)
        for i in d:
            if i[0]==p:
                ans.append(i[1])
        return ans                

