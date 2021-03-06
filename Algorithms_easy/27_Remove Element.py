class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = 0
        n = len(nums)
        
        for i in range(n):
            if nums[i] == val:
                cnt += 1
            else:
                nums[i-cnt] = nums[i]
        return n - cnt
        #遍历数组，遇val计数器加一，不遇val往后交换数字