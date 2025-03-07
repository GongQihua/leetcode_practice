import heapq
import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()

    N, E  = map(int, data[0].split())
    activation_time = [-1] * N
    visited = [False] * N

    pq = []

    for i in range(1, E+1):
        T, P = map(int, data[i].split())
        if activation_time[P] == -1:
            activation_time[P] = T
            heapq.heappush(pq, (T, P))

    while pq:
        time, pos = heapq.heappop(pq)
        if visited[pos]:
            continue
        visited[pos] = True

        next_time = time + 1

        neighbors = [(pos - 1 + N) % N, (pos + 1) % N]
        for neighbor in neighbors:
            if activation_time[neighbor] == -1 or activation_time[neighbor] > next_time:
                activation_time[neighbor] = next_time
                if not visited[neighbor]:
                    heapq.heappush(pq, (next_time, neighbor))

    max_time = max(activation_time)
    latest_engines = [i for i in range(N) if activation_time[i] == max_time]

    print(len(latest_engines))
    print(' '.join(map(str, latest_engines)))

if __name__ == '__main__':
    main()