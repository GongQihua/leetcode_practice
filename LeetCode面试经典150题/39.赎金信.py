class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        cnt = defaultdict(int)
        for c in magazine:
            cnt[c] += 1
        for c in ransomNote:
            cnt[c] -= 1
        return all(c >= 0 for c in cnt.values())