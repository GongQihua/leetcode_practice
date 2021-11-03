class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = j = res = 0
        chars = set()
        while i < len(s):
            while s[i] in chars:
                if s[j] in chars:
                        chars.remove(s[j])
                j += 1
            chars.add(s[i])
            res = max(res, i-j+1)
            i += 1
        return res
'''
“滑动窗口 + 哈希表”。
定义一个哈希表记录当前窗口内出现的字符，i、j 分别表示不重复子串的结束位置和开始位置，res 表示无重复字符子串的最大长度。
遍历 i，若 [j, i - 1] 窗口内存在 s[i]，则 j 循环向右移动，更新哈希表，直至 [j, i - 1] 窗口不存在 s[i]，循环结束。将 s[i] 加入哈希表中，此时 [j, i] 窗口内不含重复元素，更新 res 的最大值：res = max(res, i - j + 1)。
最后返回 res 即可。
'''