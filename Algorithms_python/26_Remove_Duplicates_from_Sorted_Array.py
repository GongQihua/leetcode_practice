class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        k = 0
        for x in nums:
            if k == 0 or x != nums[k - 1]:
                nums[k] = x
                k += 1
        return k
    
        #所以最终打出的数组大小是返回值，既到最大数为止
        #所以方法就是直接替换数组前N个数就行