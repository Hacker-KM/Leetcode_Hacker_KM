from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxCount = 0
        left = 0
        s = list(s)
        
        for right in range(len(s)):
            temp = s[left:right+1]
            c = Counter(temp)
            maxCharCount = max(c.values())
            replacements_needed = len(temp) - maxCharCount
            
            if replacements_needed > k:
                left += 1
            
            maxCount = max(maxCount, right - left + 1)
        
        return maxCount
