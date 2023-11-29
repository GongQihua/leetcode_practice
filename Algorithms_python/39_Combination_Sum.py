class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(i:int, s:int):
            if s == 0:
                ans.append(t[:])
                return
            if s < candidates[i]:
                return
            for j in range(i, len(candidates)):
                t.append(candidates[j])
                dfs(j, s - candidates[j])
                t.pop()
        candidates.sort()
        t = []
        ans = []
        dfs(0, target)
        return ans
'''
DFS深度搜索算法，记得设好起始点，避免重复的情况
dfs主要就是两个参数，一个搜索起始位置，一个剩余目标值
'''