class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
'''
思路：仔细观察一下矩阵的变化，每个位置会有固定的四个位置与它互换位置
所以只需要先水平翻转，然后再翻转对角线就行
ps：还有种方法，新建矩阵，挨个变换填入，然后用原矩阵复制新矩阵
'''