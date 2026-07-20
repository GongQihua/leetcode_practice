class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        res = []
        worddict = {word: i for i, word in enumerate(words)}
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                tmp1 = word[:j]
                tmp2 = word[j:]
                if tmp1[::-1] in worddict and worddict[tmp1[::-1]] != i and tmp2 == tmp2[::-1]:
                    res.append([i, worddict[tmp1[::-1]]])
                if j > 0 and tmp2[::-1] in worddict and worddict[tmp2[::-1]] != i and tmp1 == tmp1[::-1]:
                    res.append([worddict[tmp2[::-1]], i])
        return res