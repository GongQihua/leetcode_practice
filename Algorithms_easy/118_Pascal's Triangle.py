class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        t = []
        for i in range(numRows):
            t = [0 for j in range(i + 1)]
            t[0], t[-1] = 1, 1
            for j in range(1, i):
                t[j] = res[i - 1][j - 1] + res[i - 1][j]
            res.append(t)
        return res
        #杨辉三角python