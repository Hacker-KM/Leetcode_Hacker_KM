class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        l = []
        ans = []
        for i in set(words):
            l.append([words.count(i), i])
        l.sort(key=lambda x: (-x[0], x[1]))

        for i in range(k):
            ans.append(l[i][1])

        return ans
