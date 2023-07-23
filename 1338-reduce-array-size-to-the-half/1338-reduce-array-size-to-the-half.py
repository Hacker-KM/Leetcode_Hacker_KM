class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freqs=Counter(arr)
        freq= []
        for i in freqs.values():
            freq.append(i)
        freq.sort(reverse=True)
        ans = 0
        s=0
        while (len(arr)//2)>s:
            s += freq[ans]
            ans+=1
        return ans