def check(s, t, a, b):
    va = [0] * 10
    vb = [0] * 10

    for i in range(4):
        ss = s % 10
        tt = t % 10
        s //= 10
        t //= 10

        if ss == tt:
            a -= 1
        else:
            va[ss] += 1
            vb[tt] += 1
        
    for i in range(10):
        b -= min(va[i], vb[i])

    return a == 0 and b == 0

def main():
    n = int(input())
    v = []
    for i in range(n):
        tmp = [0] * 3
        s = input().split()
        tmp[0] = int(s[0])
        tmp[1] = int(s[1][0])
        tmp[2] = int(s[1][2])
        v.append(tmp)
    
    ans = []

    for val in range(10000):
        flag = True
        for lis in v:
            if not check(val, lis[0], lis[1], lis[2]):
                flag = False
                break
        if flag:
            ans.append(val)
        if len(ans) > 1:
            break
    
    if len(ans) == 1:
        print(ans[0])
    elif len(ans) > 1:
        print("NA")

if __name__ == "__main__":
    main()