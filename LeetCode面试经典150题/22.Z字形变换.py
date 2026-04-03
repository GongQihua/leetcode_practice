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
        ans = []
        for row in mat:
            for ch in row:
                if ch:
                    ans.append(ch)
        return ''.join(ans)

'''
按照题目要求打出一个数字表，然后返还数列数字，用join消除中间的空格
根据题意，当我们在矩阵上填写字符时，会向下填写 r个字符，然后向右上继续填写 r−2个字符，最后回到第一行，
因此 Z 字形变换的周期 t=r+r−2=2r−2，每个周期会占用矩阵上的 1+r−2=r−1列。
周期n/t，总共列数[n/t]*(r-1)。
'''