class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        if n < 3:
            return res
        nums.sort()
        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, n - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < n and nums[j] == nums[j - 1]:
                        j += 1
                    while k > i and nums[k] == nums[k + 1]:
                        k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        return res
'''
定三个数i,j,k，i确定首位，j为次位，k为末尾，i为首往下循环，j和k向中间靠拢，
三数累计验证是否等于0
别忘记检查数组中是否有相同数
方法基本都是三指针三循环
'''