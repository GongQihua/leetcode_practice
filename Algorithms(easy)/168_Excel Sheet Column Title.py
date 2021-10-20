class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber:
            columnNumber -= 1
            res.append(chr(ord('A') + columnNumber % 26))
            columnNumber //= 26
        return ''.join(res[: : -1])
'''
要完成ascii到a数字再转回ascii的操作，然后编辑新数列
由于从最大数开始逐个向下除，然后出数字，得出的数组是倒的
output的时候倒过来，用.join去除中间符号
'''