class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        w2c = dict()
        c2w = dict()
        words = s.split()
        if len(words) != len(pattern):
            return False

        for ch, word in zip(pattern, words):
            if (word in w2c and w2c[word] != ch) or (ch in c2w and c2w[ch] != word):
                return False
            w2c[word] = ch
            c2w[ch] = word
        return True 