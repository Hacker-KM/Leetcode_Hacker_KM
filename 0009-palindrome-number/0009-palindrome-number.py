class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        x = list(x)
        if x==x[::-1]:
            return True
        return False