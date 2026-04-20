class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0
        n = len(nums)
        while i < n:
            low = i
            i += 1
            while(i < n and nums[i] == nums[i - 1] + 1):
                i += 1
            high = i - 1
            if low < high:
                res.append(f"{nums[low]}->{nums[high]}")
            else:
                res.append(str(nums[low]))
        return res