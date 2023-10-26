class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = m - 1, 0
        while i >= 0 and j < n:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                i -= 1
            else:
                j += 1
        return False
'''
有两种方法，一种是每一行二分查找
另一种就是这个，从角开始往下找
这里我们以左下角作为起始搜索点，往右上方向开始搜索，比较当前元素 matrix[i][j]与 target 的大小关系：

若 matrix[i][j] == target，说明找到了目标值，直接返回 true。
若 matrix[i][j] > target，说明这一行从当前位置开始往右的所有元素均大于 target，应该让 i 指针往上移动，即 i--。
若 matrix[i][j] < target，说明这一列从当前位置开始往上的所有元素均小于 target，应该让 j 指针往右移动，即 j++。
若搜索结束依然找不到 target，返回 false。

时间复杂度 O(m + n)
'''