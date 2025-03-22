'''
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i: int, j: int):
            grid[i][j] = '0'
            for a, b in pairwise(dirs):
                x, y = i+a, j+b
                if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                    dfs(x, y)
        
        ans = 0
        dirs = (-1, 0, 1, 0, -1)
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    ans += 1
        return ans