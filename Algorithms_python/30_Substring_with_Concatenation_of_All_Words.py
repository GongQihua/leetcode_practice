class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        cnt = Counter(words)
        m, n = len(s), len(words)
        k = len(words[0])
        ans = []
        for i in range(k):
            cnt1 = Counter()
            l = r = i
            t = 0
            while r + k <= m:
                w = s[r : r+k]
                r += k
                if w not in cnt:
                    l = r
                    cnt1.clear()
                    t = 0
                    continue
                cnt1[w] += 1
                t += 1
                while cnt1[w] > cnt[w]:
                    remove = s[l : l+k]
                    l += k
                    cnt1[remove] -= 1
                    t -= 1
                if t == n:
                    ans.append(l)
        return ans
'''
我们用哈希表 $cnt$ 统计 $words$ 中每个单词出现的次数，用哈希表 $cnt1$ 统计当前滑动窗口中每个单词出现的次数。我们记字符串 $s$ 的长度为 $m$，字符串数组 $words$ 中单词的数量为 $n$，每个单词的长度为 $k$。

我们可以枚举滑动窗口的起点 $i$，其中 $0 \lt i \lt k$。对于每个起点，我们维护一个滑动窗口，左边界为 $l$，右边界为 $r$，滑动窗口中的单词个数为 $t$，另外用一个哈希表 $cnt1$ 统计滑动窗口中每个单词出现的次数。

每一次，我们提取字符串 $s[r:r+k]$，如果 $s[r:r+k]$ 不在哈希表 $cnt$ 中，说明当前滑动窗口中的单词不合法，我们将左边界 $l$ 更新为 $r$，同时将哈希表 $cnt1$ 清空，单词个数 $t$ 重置为 0。如果 $s[r:r+k]$ 在哈希表 $cnt$ 中，说明当前滑动窗口中的单词合法，我们将单词个数 $t$ 加 1，将哈希表 $cnt1$ 中 $s[r:r+k]$ 的次数加 1。如果 $cnt1[s[r:r+k]]$ 大于 $cnt[s[r:r+k]]$，说明当前滑动窗口中 $s[r:r+k]$ 出现的次数过多，我们需要将左边界 $l$ 右移，直到 $cnt1[s[r:r+k]] = cnt[s[r:r+k]]$。如果 $t = n$，说明当前滑动窗口中的单词正好合法，我们将左边界 $l$ 加入答案数组。

时间复杂度 $O(m \times k)$，空间复杂度 $O(n \times k)$。其中 $m$ 和 $n$ 分别是字符串 $s$ 和字符串数组 $words$ 的长度，而 $k$ 是字符串数组 $words$ 中单词的长度。
'''