# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    hashset = set()
    ans, i = 0, 0
    for j in range(n):
        while s[j] in hashset:
            hashset.remove(s[i])
            i += 1
        hashset.add(s[j])
        if ans < j - i + 1:
            output = s[i:j+1]
            ans = max(ans, j - i + 1)
    return ans, output

if __name__ == "__main__":
    s = input()
    ans, output = lengthOfLongestSubstring(s)
    print(ans, output)