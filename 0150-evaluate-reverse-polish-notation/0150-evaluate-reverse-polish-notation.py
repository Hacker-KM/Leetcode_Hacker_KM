class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i!='+' and i!= '-' and i!= '*' and i!='/':
                stack.append(int(i))
            else:
                number2 = stack.pop()
                number1 = stack.pop()
                if i=='+':
                    stack.append(number1+number2)
                elif i=='-':
                    stack.append(number1-number2)
                elif i=='*':
                    stack.append(number1*number2)
                elif i=='/':
                    stack.append(int(number1/number2))
        return stack[-1]
            