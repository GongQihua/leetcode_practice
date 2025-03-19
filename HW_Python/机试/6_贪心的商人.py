def main():
    n = int(input())
    m = int(input())
    num = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        price = list(map(int, input().split()))
        res = 0
        for j in range(m - 1):
            if price[j + 1] > price[j]:
                res += price[j + 1] - price[j]
        ans += res * num[i]
    print(ans)

if __name__ == '__main__':
    main()