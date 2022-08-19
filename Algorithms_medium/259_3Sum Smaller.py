class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans, n = 0, len(nums)
        for i in range(n):
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s >= target:
                    k -= 1
                else:
                    ans += k - j
                    j += 1
        return ans
'''
经典双指针，其中ans计数的那步+=k-j很妙，记得记一下，不然随便写又要多好几行
'''