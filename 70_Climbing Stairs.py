class Solution:
    def climbStairs(self, n: int) -> int:
        a = 0
        b = 1
        for i in range(n):
            c = a + b
            a = b
            b = c
        return b
        #递归，也就是把问题变成
        #想上第 n 级台阶，可从第 n-1 级台阶爬一级上去，也可从第 n-2 级台阶爬两级上去
        # 即：f(n) = f(n-1) + f(n-2)。f[1]就是1遍for，f[2]就是两遍，同理
