class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [True] * n
        ans = 0
        for i in range(2, n):
            if primes[i]:
                ans += 1
                for j in range(i + i, n, i):
                    primes[j] = False
        return ans

'''
算法的思路就是，如果x是质数，那么大于x的x的倍数2x,3x,… 一定不是质数。
'''