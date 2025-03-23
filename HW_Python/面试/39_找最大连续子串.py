'''
题目:
一串字符串Q由“1-10"A-Z"组成,各字符之间由”,”隔开,找到最大连续的子串。(10后面的字符是A)
示例1:
输入:
1,2,3,4,5,7,8
输出:
12345
'''
def find_max_continuous_substring(s: str) -> str:
    chars = s.split(',')
    max_substring = ""
    cur_substring = chars[0]

    for i in range(1, len(chars)):
        if ord(chars[i]) - ord(chars[i - 1]) == 1:
            cur_substring += chars[i]
        else:
            if len(cur_substring) > len(max_substring):
                max_substring = cur_substring
            cur_substring = chars[i]
    if len(cur_substring) > len(max_substring):
        max_substring = cur_substring
    return max_substring

input = "1,2,3,4,5,7,8"
result = find_max_continuous_substring(input)
print(result)  # 输出: 12345