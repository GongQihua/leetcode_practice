class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(i:int, s:int):
            if s == 0:
                ans.append(t[:])
                return
            if i >= len(candidates) or s < candidates[i]:
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                t.append(candidates[j])
                dfs(j + 1, s - candidates[j])
                t.pop()
        candidates.sort()
        t = []
        ans = []
        dfs(0, target)
        return ans
'''
相比于上一题，多一个排除重复项，记得检测重复
用if i > u and candidates[i] == candidates[i - 1]:
    continue
来检查是否与上个数重复
然后记得排序，和每次循环都要加1，dfs的时候记得i+1
'''