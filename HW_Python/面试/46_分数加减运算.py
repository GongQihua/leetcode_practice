'''
给定一个表示分数加减运算的字符串 expression ，你需要返回一个字符串形式的计算结果。 
这个结果应该是不可约分的分数，即 最简分数。 如果最终结果是一个整数，例如 2，你需要将它转换成分数形式，其分母为 1。所以在上述例子中, 2 应该被转换为 2/1。
'''
class Solution:
    def fractionAddition(self, expression: str) -> str:
        x, y = 0, 1
        i, n = 0, len(expression)
        while i < n:
            x1, sign = 0, 1
            if expression[i] == '-' or expression[i] == '+':
                if expression[i] == '-':
                    sign = -1
                i += 1
            while i < n and expression[i].isdigit():
                x1 = x1 * 10 + int(expression[i])
                i += 1
            x1 = sign * x1
            i += 1

            y1 = 0
            while i < n and expression[i].isdigit():
                y1 = y1 * 10 + int(expression[i])
                i += 1
            
            x = x * y1 + x1 * y
            y *= y1

        if x == 0:
            return "0/1"
        else:
            g = gcd(abs(x), y)
        return f"{x // g}/{y // g}"