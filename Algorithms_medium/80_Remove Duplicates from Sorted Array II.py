class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for num in nums:
            if i < 2 or num != nums[i - 2]:
                nums[i] = num
                i += 1
        return i
'''
非常简单的程序，因为题目要求很细
想法就是数组挨个检查，不能查过三位相同，直接改数组的值就行
注意刚开始几位也要列入计算的
'''