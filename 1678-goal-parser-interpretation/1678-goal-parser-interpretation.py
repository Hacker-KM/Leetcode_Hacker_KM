class Solution:
    def interpret(self, command: str) -> str:
        x= command.replace('()','o')
        x = x.replace('(','')
        x = x.replace(')','')
        return x