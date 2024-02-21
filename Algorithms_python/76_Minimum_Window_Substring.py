class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = Counter()
        cnt, j, k, mi = 0, 0, -1, inf
        for i, c in enumerate(s):
            window[c] += 1
            if need[c] >= window[c]:
                cnt += 1
            while cnt == len(t):
                if i - j + 1 < mi:
                    mi = i - j + 1
                    k = j
                if need[s[j]] >= window[s[j]]:
                    cnt -= 1
                window[s[j]] -= 1
                j += 1
        return '' if k < 0 else s[k : k + mi]
'''
我们用一个哈希表或数组 $need$ 统计字符串 $t$ 中每个字符出现的次数，用另一个哈希表或数组 $window$ 统计滑动窗口中每个字符出现的次数。另外，定义两个指针 $j$ 和 $i$ 分别指向窗口的左右边界，变量 $cnt$ 表示窗口中已经包含了 $t$ 中的多少个字符，变量 $k$ 和 $mi$ 分别表示最小覆盖子串的起始位置和长度。

我们从左到右遍历字符串 $s$，对于当前遍历到的字符 $s[i]$：

我们将其加入窗口中，即 $window[s[i]] = window[s[i]] + 1$，如果此时 $need[s[i]] \geq window[s[i]]$，则说明 $s[i]$ 是一个「必要的字符」，我们将 $cnt$ 加一。如果 $cnt$ 等于 $t$ 的长度，说明此时窗口中已经包含了 $t$ 中的所有字符，我们就可以尝试更新最小覆盖子串的起始位置和长度了。如果 $i - j + 1 \lt mi$，说明当前窗口表示的子串更短，我们就更新 $mi = i - j + 1$ 和 $k = j$。然后，我们尝试移动左边界 $j$，如果此时 $need[s[j]] \geq window[s[j]]$，则说明 $s[j]$ 是一个「必要的字符」，移动左边界时会把 $s[j]$ 这个字符从窗口中移除，因此我们需要将 $cnt$ 减一，然后更新 $window[s[j]] = window[s[j]] - 1$，并将 $j$ 右移一位。如果 $cnt$ 与 $t$ 的长度不相等，说明此时窗口中还没有包含 $t$ 中的所有字符，我们就不需要移动左边界了，直接将 $i$ 右移一位，继续遍历即可。

遍历结束，如果没有找到最小覆盖子串，返回空字符串，否则返回 $s[k:k+mi]$ 即可。

时间复杂度 $O(m + n)$，空间复杂度 $O(C)$。其中 $m$ 和 $n$ 分别是字符串 $s$ 和 $t$ 的长度；而 $C$ 是字符集的大小，本题中 $C = 128$。
'''