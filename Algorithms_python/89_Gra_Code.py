class Solution:
    def grayCode(self, n: int) -> List[int]:
        return [i ^ (i >> 1) for i in range(1 << n)]
'''
解题的关键在于这个公式 G(i) = i ^ (i/2)
紧接着一步就出来了
格雷码公式表达：
int gray(x) {
    return x ^ (x >> 1);
}
'''