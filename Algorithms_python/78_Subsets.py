class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(i: int):
            if i == len(nums):
                ans.append(t[:])
                return
            dfs(i + 1)
            t.append(nums[i])
            dfs(i + 1)
            t.pop()
        ans = []
        t = []
        dfs(0)
        return ans
'''
dfs深度搜索算法
要同时兼顾数字扩展和位数扩展两个方向，第一个dfs相当于扩展数字，第二个相当于扩展位数
要想通最直接把数字列出来，一看就懂
'''