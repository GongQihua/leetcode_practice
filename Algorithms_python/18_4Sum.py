class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        if n < 4:
            return []
        nums.sort()
        for i in range(n -3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                k = j + 1
                l = n - 1
                while k < l:
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        while k < n and nums[k] == nums[k - 1]:
                            k += 1
                        while l > j and nums[l] == nums[l + 1]:
                            l -= 1
                    elif nums[i] + nums[j] + nums[k] + nums[l] < target:
                        k += 1
                    else:
                        l -= 1
        return res
'''
于先前经历过的所有sum问题一样，排序 + 双指针来实现算法，确定几个位置，逐步推进
'''