class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        def is_letter(char):
            return 'a' <= char <= 'z' or 'A' <= char <= 'Z'
        char_list = list(s)
        left, right = 0, len(char_list) - 1
        while left < right:
            while left < right and not is_letter(char_list[left]):
                left += 1
            while left < right and not is_letter(char_list[right]):
                right -= 1
            char_list[left], char_list[right] = char_list[right], char_list[left]
            left += 1
            right -= 1
        return ''.join(char_list)
