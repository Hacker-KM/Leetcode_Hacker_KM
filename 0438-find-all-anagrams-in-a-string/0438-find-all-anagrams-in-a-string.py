class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_count = Counter(s[:len(p)])
        p_count = Counter(p)
        ans = []
        if s_count==p_count:
            ans.append(0)
        i = len(p)
        j=0
        while i<len(s):
            if s[i] in s_count:
                s_count[s[i]]+=1
            else:
                s_count[s[i]]=1
            if s_count[s[j]]==1:
                del s_count[s[j]]
            else:
                s_count[s[j]]-=1
            if s_count==p_count:
                ans.append(j+1)
            i+=1
            j+=1
        return ans