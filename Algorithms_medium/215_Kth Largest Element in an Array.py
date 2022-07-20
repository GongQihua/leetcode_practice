class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_sort(left, right, k):
            if left == right:
                return nums[left]
            i, j = left - 1, right + 1
            x = nums[(left + right) >> 1]
            while i < j:
                while 1:
                    i += 1
                    if nums[i] >= x:
                        break
                while 1:
                    j -= 1
                    if nums[j] <= x:
                        break
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
            if j < k:
                return quick_sort(j + 1, right, k)
            return quick_sort(left, j, k)

        n = len(nums)
        return quick_sort(0, n - 1, n - k)

'''
方法一：直接sort数组返回反向排序的第k个数，但是时间复杂度有O(nlogn)
方法二：也就是这里用的快速排序
并不是所有时候，都需要整个数组进入有序状态，只需要局部有序，或者说，从大到小排序，只要0 ... k位置的元素有序，那么就能确定结果，此处使用快速排序。
快速排序有一特点，每一次循环结束时，能够确定的是partition一定处于它该处于的索引位置。从而根据它得知，结果值是在左数组还是在右数组当中，然后对那一数组进行排序即可。
算法复杂度O(n)
'''