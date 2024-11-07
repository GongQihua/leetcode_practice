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
# 做法二：贪心

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        i = 0
        while i < n:
            sum_of_gas = sum_of_cost = 0
            cnt = 0
            while cnt < n:
                j = (i + cnt) % n
                sum_of_gas += gas[j]
                sum_of_cost += cost[j]
                if sum_of_cost > sum_of_gas:
                    break
                cnt += 1
            if cnt == n:
                return i
            else:
                i += cnt + 1
        return -1

'''
贪心不等式推导推导中，能够得出结论：从 x,y 之间的任何一个加油站出发，都无法到达加油站 y 的下一个加油站。

在发现了这一个性质后，算法就很清楚了：我们首先检查第 0 个加油站，并试图判断能否环绕一周；如果不能，就从第一个无法到达的加油站开始继续检查。
'''