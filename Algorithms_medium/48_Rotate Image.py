class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        s, n = 0, len(matrix)
        while s < (n >> 1):
            e = n - s - 1
            for i in range(s, e):
                x = n - i - 1
                t = matrix[i][e]
                matrix[i][e] = matrix[s][i]
                matrix[s][i] = matrix[x][s]
                matrix[x][s] = matrix[e][x]
                matrix[e][x] = t
            s += 1
        return matrix
'''
思路：仔细观察一下矩阵的变化，每个位置会有固定的四个位置与它互换位置
例如四个顶点，1234，就是1和2换，2和3换，3和4换，最后4和1换
按这个互换的方法解题
'''