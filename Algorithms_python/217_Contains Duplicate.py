class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False

'''
排序数组，然后两个相邻元素是否相同即可
还有一种解法，遍历元素并记录，当第二次出现时，直接返回 true，就是哈希表
'''