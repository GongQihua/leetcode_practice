from collections import defaultdict
from collections import deque

def solve():
    g = defaultdict(list)
    m = int(input())
    N = int(1e6+5)
    n = 0
    du = [0] * N
    val = [0] * N

    while m:
        m -= 1
        u, v, w = map(int, input().split())
        n = max(n, max(u, v))
        g[u].append(v)
        du[v] += 1
        val[u] += w
    q = deque()

    for i in range(n+1):
        if du[i] == 0:
            q.append(i)

    while q:
        u = q.popleft()
        for v in g[u]:
            du[v] -= 1
            val[v] += val[u] //100 * 15
            if du[v] == 0:
                q.append(v)
        if len(q) == 0:
            print(u, val[u])

if __name__ == '__main__':
    solve()