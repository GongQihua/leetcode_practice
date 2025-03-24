import math
def gcd(a: int, b: int):
    while b:
        a, b = b, a % b
    return a

def lcm(a: int, b: int):
    return a * b // gcd(a, b)

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(lcm(a, b))