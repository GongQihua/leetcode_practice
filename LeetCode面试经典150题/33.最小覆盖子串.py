class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ori = Counter(t)
        cnt = Counter()

        def check():
            for ch, need in ori.items():
                if cnt[ch] < need:
                    return False
            return True

        l, r = 0, -1
        min_len = float('inf')
        ans = -1

        while r < len(s):
            r += 1
            if r >= len(s):
                break
            if s[r] in ori:
                cnt[s[r]] += 1

            while check() and l <= r:
                current_len = r - l + 1
                if current_len < min_len:
                    min_len = current_len
                    ans = l

                if s[l] in ori:
                    cnt[s[l]] -= 1
                l += 1
        if ans == -1:
            return ""
        return s[ans: ans + min_len]