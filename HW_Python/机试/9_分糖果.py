def min_step(candies):
    steps = 0
    while candies > 1:
        if candies % 2 == 0:
            candies //= 2
        else:
            if candies == 3 or (candies & 2) == 0:
                candies -= 1
            else:
                candies += 1
        steps += 1
    return steps

if __name__ == "__main__":
    steps = min_step(int(input()))
    print(steps)