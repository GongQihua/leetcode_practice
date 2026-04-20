class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current = num
                current_len = 1

                while current + 1 in num_set:
                    current += 1
                    current_len += 1

                res = max(res, current_len)
        return res