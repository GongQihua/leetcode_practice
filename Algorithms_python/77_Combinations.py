class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(i: int):
            if len(t) == k:
                ans.append(t[:])
                return
            if i > n:
                return
            for j in range(i, n + 1):
                t.append(j)
                dfs(j + 1)
                t.pop()
                
        ans = []
        t = []
        dfs(1)
        return ans
'''
DFS,每次扩展一位，往下深挖，然后移除最后一位，这样就能保证能出所有可能性
更新：简化了dfs的逻辑，现在只用传一个参数i
'''