# class Solution:
#     def canMakeSubsequence(self, str1: str, str2: str) -> bool:

        # str1 = list(str1)
        # str2 = list(str2)
        # l = []
        # for i in str2:
        #     if i not in str1:
        #         l.append(i)
        # for i in l:
        #     prev_char = chr(((ord(i) - ord('a') - 1) % 26) + ord('a'))
        #     if prev_char not in str1:
        #         return False
        #     else:
        #         str1.remove(prev_char)

        # return True
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        j = i = 0
        while i < len(str1) and j < len(str2):
            c1, c2 = str1[i], str2[j]
            if ord(c1) == ord(c2) or ord(c1) == ord(c2) - 1 or (c1 == "z" and c2 == "a"): j += 1
            i += 1
        return j == len(str2)
