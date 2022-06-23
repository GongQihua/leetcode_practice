class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total, cur = 0, 0
        start = 0
        for i in range(n):
            total += gas[i] - cost[i]
            cur += gas[i] - cost[i]
            if cur < 0:
                start = i + 1
                cur = 0
        if total >= 0:
            return start
        else:
            return -1

'''
设定三个参数，现油量，总油量和起始点，就能解这题了
'''