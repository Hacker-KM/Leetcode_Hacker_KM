class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k = 1
        ans = 0
        while word*k in sequence and len(sequence)>=len(word):
            k+=1
            ans+=1
        return ans