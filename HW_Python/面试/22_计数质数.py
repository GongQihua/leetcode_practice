# 给定整数 n ，返回 所有小于非负整数 n 的质数的数量 。
class Solution1:
    def countPrimes(self, n: int) -> int: # 暴力
        ans = 0
        for i in range(2, n):
            ans += self.isPrime(i)
        return ans
    
    def isPrime(self, x: int):
        i = 2
        while i * i <= x:
            if x % i == 0:
                return 0
            i += 1
        return 1

class Solution2:
    def countPrimes(self, n: int) -> int: # 埃氏筛
        primes = [True] * n
        ans = 0
        for i in range(2, n):
            if primes[i]:
                ans += 1
                for j in range(i * i, n, i):
                    primes[j] = False
        return ans