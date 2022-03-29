class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        zero_rows = [False] * m
        zero_cols = [False] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_rows[i] = zero_cols[j] = True
        for i in range(m):
            for j in range(n):
                if zero_rows[i] or zero_cols[j]:
                    matrix[i][j] = 0
'''
因为不能重创一个矩阵返回，所以要在原基础上改
用两个数组标记每一行、每一列是否出现零。
遍历原数组，若元素为0，将元素所在的行、列所对应的标记数组的位置为 true。
最后遍历原数组，用标记数组更新原数组。
'''