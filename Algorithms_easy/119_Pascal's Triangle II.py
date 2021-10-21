class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1 for k in range(0, rowIndex + 1)]
        for i in range(2, rowIndex + 1):
            for j in range(i-1, 0, -1):
                row[j] += row[j-1]
                print(row)
        return row
'''
杨辉三角累加法，先打出一个全是1的list
例：输入4， 
分步output为：
[1, 2, 1, 1, 1]
[1, 2, 3, 1, 1]
[1, 3, 3, 1, 1]
[1, 3, 3, 4, 1]
[1, 3, 6, 4, 1]
[1, 4, 6, 4, 1]
很直观了，不bb解释了
'''