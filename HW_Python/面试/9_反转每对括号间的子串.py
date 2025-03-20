'''
给出一个字符串 s（仅含有小写英文字母和括号）。
请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。
注意，您的结果中 不应 包含任何括号。
'''
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch != ')':
                stack.append(ch)
            else:
                tmp = []
                while stack and stack[-1] != '(':
                    tmp.append(stack.pop())
                if stack:
                    stack.pop()
                stack += tmp
        return "".join(stack)
    
    def reverseParentheses2(self, s: str) -> str: # 预处理括号的做法
        n = len(s)
        pair = [0] * n  # 用于记录括号的匹配关系
        stack = []  # 用列表模拟栈

        # 第一步：记录每个括号的匹配位置
        for i in range(n):
            if s[i] == '(':
                stack.append(i)  # 将左括号的索引压栈
            elif s[i] == ')':
                j = stack.pop()  # 弹出匹配的左括号索引
                pair[i] = j  # 记录右括号对应的左括号位置
                pair[j] = i  # 记录左括号对应的右括号位置

        # 第二步：遍历字符串，根据括号匹配关系改变方向
        ret = []  # 用于存储结果
        index = 0  # 当前遍历的索引
        step = 1   # 遍历方向：1 表示从左到右，-1 表示从右到左

        while index < n:
            if s[index] == '(' or s[index] == ')':
                # 遇到括号，跳转到匹配的括号位置，并改变方向
                index = pair[index]
                step = -step
            else:
                # 普通字符，直接添加到结果中
                ret.append(s[index])
            index += step  # 移动到下一个字符

        return ''.join(ret)  # 将列表转换为字符串