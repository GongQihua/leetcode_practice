class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            if numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]
'''
头尾各设一个指针，向中间靠拢，并时刻检验相加答案
因为规定了数列一定从小到大，所以可以判断条件< = > target
'''