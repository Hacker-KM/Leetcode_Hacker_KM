class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        lst=[pref[0]]
        for i in range(len(pref)-1):
            lst.append(pref[i]^pref[i+1])
        return lst
