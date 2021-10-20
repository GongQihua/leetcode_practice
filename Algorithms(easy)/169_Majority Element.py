class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        major = nums[len(nums) // 2]
        return major
'''
用到排序功能，.sort可以重新排序数组
因为major element一定超过一半，所以重新排序后的中位数必定就是它
'''