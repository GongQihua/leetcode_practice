class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        candidates.sort()
        def dfs(s, u, t):
            if s == target:
                ans.append(t.copy())
                return
            if s > target:
                return
            for i in range(u, n):
                if i > u and candidates[i] == candidates[i - 1]:
                    continue
                c = candidates[i]
                t.append(c)
                dfs(s+c, i+1, t)
                t.pop()
        dfs(0, 0, [])
        return ans
'''
相比于1的几个注意点，首先排除重复，用
if i > u and candidates[i] == candidates[i - 1]:
    continue
来检查是否与上个数重复
然后记得排序，和每次循环都要加1，dfs的时候记得i+1
'''