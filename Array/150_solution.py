class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.isnumeric() or token.replace("-", "").isnumeric():
                stack.append(token)
                continue
            num2 = stack.pop()
            num1 = stack.pop()
            if token == "+":
                new_number = int(num1) + int(num2)
            elif token == "-":
                new_number = int(num1) - int(num2)
            elif token == "*":
                new_number = int(num1) * int(num2)
            elif token == "/":
                new_number = int(num1) / int(num2)
            stack.append(new_number)
        return int(stack[0])


