class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n, r = len(s), numRows
        if r == 1 or r >= n:
            return s
        t = r * 2 - 2
        c = (n + t - 1) // t * (r - 1)
        mat = [[''] * c for _ in range(r)]
        x, y = 0, 0
        for i, ch in enumerate(s):
            mat[x][y] = ch
            if i % t < r - 1:
                x += 1
            else:
                x -= 1
                y += 1
        return ''.join(ch for row in mat for ch in row if ch)

'''
按照题目要求打出一个数字表，然后返还数列数字，用join消除中间的空格
根据题意，当我们在矩阵上填写字符时，会向下填写 r个字符，然后向右上继续填写 r−2个字符，最后回到第一行，
因此 Z 字形变换的周期 t=r+r−2=2r−2，每个周期会占用矩阵上的 1+r−2=r−1列。
周期n/t，总共列数[n/t]*(r-1)。
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        r = numRows
        if r == 1 or r >= len(s):
            return s
        mat = [[] for _ in range(r)]
        t, x = r * 2 - 2, 0
        for i, ch in enumerate(s):
            mat[x].append(ch)
            x += 1 if i % t < r - 1 else -1
        return ''.join(chain(*mat))#处理格式
    
'''
优化上述方法，本质就是不要管那些空格，一边输出数字表一边打印字符串。
比如一个4列的结果，直接先分四列，输入一定是1-2-3-4-3-2-1这样，按这个顺序append
坏处是要用chain处理格式，是要额外import包的
'''