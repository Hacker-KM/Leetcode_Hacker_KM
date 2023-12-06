from itertools import permutations

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        test = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        result = list(permutations(test, len(pattern) + 1))
        l = []

        for i in result:
            temp = 0
            for j in range(len(i) - 1):
                if pattern[temp] == "I" and int(i[j]) > int(i[j + 1]):
                    break
                elif pattern[temp] == "D" and int(i[j]) < int(i[j + 1]):
                    break
                else:
                    temp += 1
            else:
                l.append("".join(i))
                
        l.sort()
        return l[0]