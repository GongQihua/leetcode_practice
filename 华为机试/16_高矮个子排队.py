def main():
    try:
        a = list(map(int, input().split()))
        n, f = len(a), True

        for i in range(n - 1):
            if a[i] != a[i + 1] and (a[i] > a[i+1]) != f:
                a[i], a[i+1] = a[i+1], a[i]
            f = not f
        ans = map(str, a)
        print(' '.join(ans))
    except ValueError:
        print("[]")

if __name__ == '__main__':
    main()