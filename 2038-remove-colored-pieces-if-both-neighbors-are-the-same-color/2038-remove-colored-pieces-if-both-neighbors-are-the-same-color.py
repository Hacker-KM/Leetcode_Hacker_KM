class Solution:
    def winnerOfGame(self, colors: str) -> bool:

        # TLE

        # A_turn = True
        # while "AAA" in colors and "BBB" in colors:
        #     if A_turn:
        #         colors = colors.replace("AAA", "AA", 1)
        #     else:
        #         colors = colors.replace("BBB", "BB", 1)
        #     A_turn = not A_turn  
        # return "AAA" in colors

        A_score = B_score = 0
        for i in range(1,len(colors)-1):
            prev = colors[i-1]
            nextt = colors[i+1]
            if prev == nextt == colors[i] == "A":
                A_score+=1
            elif prev == nextt == colors[i] == "B":
                B_score+=1
        return A_score>B_score