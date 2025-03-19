def main():
    a = input().split(',')
    b = input().split(',')
    ans = []


    for x in a:
        p = ''.join(sorted(set(x)))
        match = False

        for y in b:
            q = ''.join(sorted(set(y)))
            if p ==q:
                ans.append(y)
                match = True

        if not match:
            ans.append('not found')

    print(','.join(ans))

if __name__ == '__main__':
    main()