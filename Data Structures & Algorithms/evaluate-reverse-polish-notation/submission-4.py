class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        total = 0
        for token in tokens:
            if stack and token in "+*-/":
                right = stack.pop()
                left = stack.pop()
                if token == "+":
                    total = left + right
                if token == "-":
                    total = left - right
                if token == "*":
                    total = left * right
                if token == "/":
                    total = left / right
                    total = int(total)
                stack.append(total)
            else:
                stack.append(int(token))
        return stack[-1]
