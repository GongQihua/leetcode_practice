def find(x):
    global f
    while x != f[x]:
        f[x] = f[f[x]]
        x = f[x]
    return x

def merge(x, y):
    fx, fy = find(x), find(y)
    if fx != fy:
        sz[fy] += sz[fx]
        f[fx] = fy

def main():
    global f, sz
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    
    f = [i for i in range(n * m)]
    sz = [1] * (n * m)

    offset = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for i in range(n):
        for j in range(m):
            for offsetX, offsetY in offset:
                newI = i + offsetX
                newJ = j + offsetY
                if 0 <= newI < n and 0 <= newJ < m and abs(a[i][j] - a[newI][newJ]) <= 1:
                    merge(i * m + j, newI * m + newJ)

    ans = 1

    for i in range(n * m):
        ans = max(ans, sz[find(i)])
    
    print(ans)

if __name__ == "__main__":
    main()