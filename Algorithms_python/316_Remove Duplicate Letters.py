class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        left = Counter(s)
        ans = []
        in_ans = set()
        for c in s:
            left[c] -= 1
            if c in in_ans:
                continue
            while ans and c < ans[-1] and left[ans[-1]]:
                in_ans.remove(ans.pop())
            ans.append(c)
            in_ans.add(c)
        return ''.join(ans)