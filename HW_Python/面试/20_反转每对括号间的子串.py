#给出一个字符串 s（仅含有小写英文字母和括号）。请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk = []
        current_str = ""
        for ch in s:
            if ch == '(':
                stk.append(current_str)
                current_str = ""
            elif ch == ')':
                current_str = current_str[::-1]
                current_str = stk.pop() + current_str
            else:
                current_str += ch
        return current_str