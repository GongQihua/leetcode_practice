from collections import deque

def check(index, num, father):
    global result
    if index < len(nums) and nums[index] != -1:
        nums[index] += nums[father]
        queue.append(index)
        result = max(result, nums[index])

if __name__ == '__main__':
    input_str = input()
    temp2 = input_str.split(" ")
    nums = [int(num) for num in temp2]

    queue = deque()
    result = 0

    queue.append(0)
    while queue:
        father = queue.popleft()
        check(2 * father + 1, nums, father)
        check(2 * father + 2, nums, father)

    print(result)