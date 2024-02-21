class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j, k = -1, len(nums), 0
        while k < j:
            if nums[k] == 0:
                i += 1
                nums[k], nums[i] = nums[i], nums[k]
                k += 1
            elif nums[k] == 2:
                j -= 1
                nums[k], nums[j] = nums[j], nums[k]
                k += 1
            else:
                k += 1
'''
数组元素只存在 0、1 和 2 三种，因此将 0 移动至数组头部,2 移动至数组尾部，排序便完成了。
安排两个变量，分别指向数组头部与尾部。
遍历数组，分三种情况：
与头指针数值交换，并向前一步，遍历指针向前。
与尾指针数值交换，并向后一步。遍历指针不变（还需要处理交换上来的数值）。
遍历指针向前。
'''