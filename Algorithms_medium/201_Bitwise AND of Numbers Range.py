class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right &= (right - 1)
        return right

'''
写法很简单，关键是读懂题目
题目可以转换为求数字的公共二进制前缀。然后就是这个写法了
'''