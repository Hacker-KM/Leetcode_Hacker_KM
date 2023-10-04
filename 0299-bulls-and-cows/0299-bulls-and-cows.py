class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A = B = 0
        secret = list(secret)
        guess = list(guess)

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A += 1
                secret[i] = guess[i] = '-'

        for i in range(len(secret)):
            if secret[i] != '-' and secret[i] in guess:
                B += 1
                guess[guess.index(secret[i])] = '-'

        return str(A) + "A" + str(B) + "B"
