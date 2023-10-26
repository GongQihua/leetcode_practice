class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        if n < 2 or k == 0:
            return
        nums[:] = nums[:: -1]
        #print(nums)
        nums[:k] = nums[:k][:: -1]
        nums[k:] = nums[k:][::-1]

'''
跟做过的题很像，主要先找到反转的点，这里方法比较巧妙，先盗跖，然后在反转的点分左右两边，再挨个反转就好
'''