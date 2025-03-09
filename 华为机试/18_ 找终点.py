def main():
    a = list(map(int, input().split()))
    n = len(a)
    ans = 10 ** 9

    for i in range(1, n // 2):
        ret, x = 1, i
        while x != n - 1:
            x += a[x]
            if x > n - 1:
                ret = 10 ** 9
                break
            ret += 1
        ans = min(ans, ret)
    if ans == 10 ** 9:
        ans = -1
    print(ans)

if __name__ == '__main__':
    main()