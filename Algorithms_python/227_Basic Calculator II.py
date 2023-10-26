class Solution:
    def calculate(self, s: str) -> int:
        num, n = 0, len(s)
        sign = '+'
        stack = []
        for i in range(n):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if i == n - 1 or (not s[i].isdigit() and s[i] != ' '):
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(stack.pop() / num))
                sign = s[i]
                num = 0
        res = 0
        while stack:
            res += stack.pop()
        return res
'''
用栈来进行操作，记录非数字的符号
加号：将数字压入栈；
减号：将数字的相反数压入栈；
乘除号：计算数字与栈顶元素，并将栈顶元素替换为计算结果。
'''