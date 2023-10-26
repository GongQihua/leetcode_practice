from sortedcontainers import SortedSet
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        s = SortedSet()
        for i, num in enumerate(nums):
            idx = s.bisect_left(num - t)
            if 0 <= idx < len(s) and s[idx] <= num + t:
                return True
            s.add(num)
            if i >= k:
                s.remove(nums[i - k])
        return False

'''
跟上一题思路几乎是一样的，但因为条件限制多了，这里用“滑动窗口 + 有序集合”实现
'''