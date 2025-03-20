# 查找一个数组Q中出现最多次数的值，如果存在相同的数量按大的值输出。
def find_most_frequent(arr):
    count_dict = {}
    for i in arr:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    max_count = max(count_dict.values())
    max_num = max([k for k, v in count_dict.items() if v == max_count])
    return max_num

if __name__ == '__main__':
    arr = input().split(" ")
    print(find_most_frequent(arr))