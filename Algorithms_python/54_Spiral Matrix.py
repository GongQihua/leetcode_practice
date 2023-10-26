class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def add(i1, j1, i2, j2):
            if i1 == i2:
                return [matrix[i1][j] for j in range(j1, j2+1)]
            if j1 == j2:
                return [matrix[i][j1] for i in range(i1, i2+1)]
            return [matrix[i1][j] for j in range(j1, j2)] + [matrix[i][j2] for i in range(i1, i2)] + [matrix[i2][j] for j in range(j2, j1, -1)] + [matrix[i][j1] for i in range(i2, i1, -1)]
        
        m, n = len(matrix), len(matrix[0])
        i1, j1, i2, j2 = 0, 0, m-1, n-1
        res = []
        while i1 <= i2 and j1 <= j2:
            res += add(i1, j1, i2, j2)
            i1, j1, i2, j2 = i1+1, j1+1, i2-1, j2-1
        return res
'''
算是个暴力解，根据题目的顺序绕圈，从外圈往里走，直接累加
两点要注意，一是观察matrix[][]里两数变化的规律，循环别写错
二是矩阵中间项，循环时的范围，不要出错
'''