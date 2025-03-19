# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
from typing import List
def permute(self, nums: List[int]) -> List[List[int]]:
    def dfs(first):
        if first == n:
            ans.append(nums[:])
        for i in range(first, n):
            nums[first], nums[i] = nums[i], nums[first]
            dfs(first + 1)
            nums[first], nums[i] = nums[i], nums[first]

    n = len(nums)
    ans = []
    dfs(0)
    return ans

if __name__ == '__main__':
    nums = [1, 2, 3]
    print(permute(None, nums))