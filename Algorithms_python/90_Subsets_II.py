class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(u, t):
            ans.append(t[:])
            for i in range(u, len(nums)):
                if i != u and nums[i] == nums[i - 1]:
                    continue
                t.append(nums[i])
                dfs(i + 1, t)
                t.pop()

        ans = []
        nums.sort()
        dfs(0, [])
        return ans
'''
dfs搜索，与同类型的题目相似，不多做解释了
就是要记得整理数组，因为这是可重复数组
'''