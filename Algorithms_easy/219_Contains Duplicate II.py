class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = {}
        for i, v in enumerate(nums):
            if v in mp and i - mp[v] <= k:
                return True
            mp[v] = i
            #print(mp)
        return False

'''
设计一个字典集合，同时显示值和位置的，值相等的话，再对比位置
'''