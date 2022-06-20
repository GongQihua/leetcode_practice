class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s, res = set(nums), 0
        for num in nums:
            if num - 1 not in s:
                t, next = 1, num + 1
                while next in s:
                    t, next = t + 1, next + 1
                res = max(res, t)
        return res

'''
第一种最简单的不管复杂度的方法就是，首先sort排序，然后两个比较，差1，再看有几个数
这里选用一种较难的方法，哈希表
具体思路：
设 res 表示连续序列的最大长度，初始为 0。哈希表 s 存放数组出现的每个元素。
遍历数组，以当前遍历到的元素 nums[i] 做为起点，循环判断 nums[i] + 1，nums[i] + 2 ... 是否存在 s 中，并不断更新连续序列的最大长度。
在这个过程中，如果 nums[i], nums[i] + 1, nums[i + 2], ... 是一个连续序列，遍历下个元素 nums[i] + 1 时，其实无需再重复循环。因此，只需要判断 nums[i] - 1 是否在 s 中，是则直接跳过。
此方法时间复杂度 O(n)，空间复杂度 O(n)。
在nums变成set集合后就可以直接if in/ not in的操作，相当于查找
'''