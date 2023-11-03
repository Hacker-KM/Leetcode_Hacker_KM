class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        if n==0:
            return []
        l = []
        temp = [words[0]]
        for i in range(1,n):
            if groups[i]!=groups[i-1]:
                temp.append(words[i])
        if len(temp)>len(l):
            l = temp
        return l
