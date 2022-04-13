def func(input):

    # please define the python3 input here. For example: a,b = map(int, input().strip().split())
    # please finish the function body here.
    # please define the python3 output here. For example: print().
    n = len(input)
    word, count = 1, 0
    for i in range(0, n):
        if input[i] == ' ':
            word += 1
            continue
        else:
            count += 1
    print('word = ',word)
    print('count = ', count)
    output = count / word
    print('%.2f' %output)

if __name__ == "__main__":
    input = 'Who Love Solo'
    func(input)