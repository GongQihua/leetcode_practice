def main():
    lis = list(map(int, input().split()))
    tim = int(input())
    if tim < len(lis):
        print(0)
        return
    l, r, ans = 1, 10000, 10000
    while l <= r:
        mid = (l + r) // 2
        waste_time = 0
        for x in lis:
            waste_time += (x + mid - 1) // mid
        if waste_time <= tim:
            ans = min(ans, mid)
            r = mid - 1
        else:
            l = mid + 1
    print(ans)

if __name__ == '__main__':
    main()