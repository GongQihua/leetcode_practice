# 求1到n的最小公倍数
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i // gcd(result, i)
    return result

if __name__ == "__main__":
    n = int(input())
    ans = lcm(n)
    print(ans)