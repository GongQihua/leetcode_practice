class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if len(token) > 1 or token[0].isdigit():
                stack.append(int(token))
                continue

            x = stack.pop()
            if token == '+':
                stack[-1] += x
            elif token == '-':
                stack[-1] -= x
            elif token == '*':
                stack[-1] *= x
            else:
                y = stack[-1]
                q, r = divmod(y, x)
                if r and x * y < 0:
                    q += 1
                stack[-1] = q
        return stack[0]