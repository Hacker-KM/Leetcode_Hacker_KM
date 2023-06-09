class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        p = sorted(letters)
        for i in p:
            if i>target:
                return i
        return letters[0] 