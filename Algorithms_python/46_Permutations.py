class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        path = [0] * n
        used = [False] * n
        def dfs(u):
            if u == n:
                res.append(path.copy())
                return
            for i in range(n):
                if not used[i]:
                    path[u] = nums[i]
                    used[i] = True
                    dfs(u + 1)
                    used[i] = False
                    
        dfs(0)
        return res
'''
dfs深度搜索算法，一层层往下枚举
我们设计一个函数dfs(i)表示已经填完了前i个位置，现在需要填第i+1个位置。
枚举所有可能的数，如果这个数没有被填过，就填入这个数，然后继续填下一个位置，直到填完所有的位置。
'''