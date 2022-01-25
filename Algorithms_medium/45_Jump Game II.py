class Solution:
    def jump(self, nums: List[int]) -> int:
        end = mx = step = 0
        for i, num in enumerate(nums[:-1]):
            mx = max(mx, i + num)
            if i == end:
                end = mx
                step += 1
        return step
'''
贪心算法
倒序数组，从最后一位往前找最大数，找一个算一步，统计步数
'''