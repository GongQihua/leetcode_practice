class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def dfs(k):
            nonlocal ok
            if k == len(t):
                ok = True
                return
            i, j = t[k]
            for v in range(9):
                if row[i][v] == col[j][v] == block[i // 3][j // 3][v] == False:
                    row[i][v] = col[j][v] = block[i // 3][j // 3][v] = True
                    board[i][j] = str(v + 1)
                    dfs(k + 1)
                    row[i][v] = col[j][v] = block[i // 3][j // 3][v] = False
                if ok:
                    return

        row = [[False] * 9 for _ in range(9)]
        col = [[False] * 9 for _ in range(9)]
        block = [[[False] * 9 for _ in range(3)] for _ in range(3)]
        t = []
        ok = False
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    t.append((i, j))
                else:
                    v = int(board[i][j]) - 1
                    row[i][v] = col[j][v] = block[i // 3][j // 3][v] = True
        dfs(0)
'''
我们用数组 row、col、box 分别记录每一行、每一列、每个 3x3 宫格中数字是否出现过。如果数字 i 在第 r 行、第 c 列、第 b 个 3x3 宫格中出现过，那么 row[r][i]、col[c][i]、box[b][i] 都为 true。

我们遍历 board 的每一个空格，枚举它可以填入的数字 v，如果 v 在当前行、当前列、当前 3x3 宫格中没有出现过，那么我们就可以尝试填入数字 v，并继续搜索下一个空格。如果搜索到最后，所有空格填充完毕，那么就说明找到了一个可行解。
'''