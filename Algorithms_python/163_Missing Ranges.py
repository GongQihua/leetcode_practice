class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        def formate(lower, upper):
            if lower == upper:
                return str(lower)
            return str(lower) + "->" + str(upper)
        
        result = []
        pre = lower - 1
        for i in range(len(nums) + 1):
            cur = nums[i] if i < len(nums) else upper + 1
            if pre + 1 <= cur - 1:
                result.append(formate(pre + 1, cur - 1))
            pre = cur
        return result

'''
返回前后两个数然后打印格式，注意那段格式输出的写法就行
'''