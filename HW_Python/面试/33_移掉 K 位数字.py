'''
给你一个以字符串表示的非负整数 num 和一个整数 k ，移除这个数中的 k 位数字，使得剩下的数字最小。请你以字符串形式返回这个最小的数字。
'''
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        numstack = []
        for digit in num:
            while k and numstack and numstack[-1] > digit:
                numstack.pop()
                k -= 1
            numstack.append(digit)
        finalstack = numstack[:-k] if k else numstack
        return "".join(numstack).lstrip("0") or "0"