'''
给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
'''
from typing import List
from functools import cmp_to_key
class Solution:
    def largestNumber1(self, nums: List[int]) -> str:
        nums_str = list(map(str, nums))

        for i in range(len(nums_str)):
            for j in range(i + 1, len(nums_str)):
                if nums_str[i] + nums_str[j] < nums_str[j] + nums_str[i]:
                    nums_str[i], nums_str[j] = nums_str[j], nums_str[i]
        if nums_str[0] == '0':
            return '0'
        return ''.join(nums_str)
    
    def largestNumber2(self, nums: List[int]) -> str:
        nums_str = list(map(str, nums))
        nums_str.sort(key=cmp_to_key(lambda x, y :1 if x + y < y + x else -1))
        if nums_str[0] == '0':
            return '0'
        return ''.join(nums_str)
    
    def largestNumber3(self, nums: List[int]) -> str:
        class customStr(str):
            def __lt__(self, other):
                return self + other < other + self
        nums_str = [customStr(num) for num in nums]
        nums_str.sort(reverse=True)
        if nums_str[0] == '0':
            return '0'
        return ''.join(nums_str)