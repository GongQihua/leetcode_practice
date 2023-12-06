class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        path = [0] * n
        used = [False] * n
        nums.sort()

        def dfs(u):
            if u == n:
                res.append(path.copy())
                return
            for i in range(n):
                if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                    continue
                path[u] = nums[i]
                used[i] = True
                dfs(u + 1)
                used[i] = False

        dfs(0)
        return res
'''
dfs深度搜索，于上一道题一样，区别是记得首先整理数组，然后dfs的时候检查是否有重复
具体多两步：
1.需要重新排列数组，从小到大
2.在循环dfs的时候要检查数组里的数是否和上一位相同
'''