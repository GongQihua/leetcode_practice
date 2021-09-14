class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        count = 0
        for i in range(len(nums)):
            if nums[count] != nums[i]:
                count += 1
                nums[count] = nums[i]
                
        return count+1
        #给的judge程序里有一行 int k = removeDuplicates(nums)
        #所以最终打出的数组大小是返回值，既到最大数为止
        #所以方法就是直接替换数组前N个数就行