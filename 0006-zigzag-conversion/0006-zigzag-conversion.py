class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        matrix = [[] for i in range(numRows)]
        j = 0
        i=0
        while i<len(s):
            if j<numRows-1:
                matrix[j].append(s[i])
                i+=1
                j+=1
            elif j==numRows-1:
                while j>0 and i<len(s):
                    matrix[j].append(s[i])
                    j-=1
                    i+=1
        print(matrix)
        s = ""
        for i in matrix:
            s1 = "".join(i)
            s+=s1

        return s
