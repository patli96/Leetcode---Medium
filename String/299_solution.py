class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0

        secret_s = ''
        guess_s = ''

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                secret_s += 'X'
                guess_s += 'X'
            else:
                secret_s += secret[i]
                guess_s += guess[i]

        for i in range(len(secret)):
            if secret_s[i] != 'X' and secret_s[i] in guess_s:
                cows += 1
                guess_s = guess_s.replace(secret_s[i], 'X', 1)

        return str(bulls) + 'A' + str(cows) + 'B'