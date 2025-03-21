# 判断一个数能否分解为几个连续自然数之和
def isConsecutiveNaturalNumbersSum(n): # n = k * (a + a + k - 1) // 2
    sequences = []
    k = 2
    while k * (k-1) // 2 < n:
        numerate = n - k * (k-1) // 2
        if numerate % k == 0:
            a = numerate // k
            if a > 0:
                sequence = list(range(a, a + k))
                sequences.append(sequence)
        k += 1
    if not sequences:
        return False
    
    return sequences

if __name__ == '__main__':
    n = 15
    print(isConsecutiveNaturalNumbersSum(n))