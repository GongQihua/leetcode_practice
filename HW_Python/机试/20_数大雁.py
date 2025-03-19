from collections import deque

def main(s : str) -> int:
    q = u = a = c = k = 0
    max_duck = 0
    Q = deque()
    cnt = [0] * (len(s) + 1)

    for i in range(len(s)):
        cnt[i+1] = cnt[i]

        if s[i] == 'q':
            q += 1
            Q.append(i)
        elif s[i] == 'u' and q > u:
            u += 1
        elif s[i] == 'a' and u > a:
            a += 1
        elif s[i] == 'c' and a > c:
            c += 1
        elif s[i] == 'k' and c > k:
           k += 1
           cnt[i+1] += 1

           q_first = Q.popleft()
           max_duck = max(max_duck, cnt[i+1] - cnt[q_first])
        elif s[i] not in 'uack':
            return -1
    return max_duck if max_duck > 0 else -1

if __name__ == '__main__':
    s = input().strip()
    print(main(s))