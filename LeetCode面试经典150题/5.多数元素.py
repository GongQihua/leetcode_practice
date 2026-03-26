from collections import defaultdict, Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        major = 0
        cnt = 0
        for num in nums:
            counter[num] += 1
            if counter[num] > cnt:
                major = num
                cnt = counter[num]
        return major
    
    def majorityElement2(self, nums: List[int]) -> int: #简单写法
        counts = Counter(nums)
        return max(counts.keys(), key=counts.get)