class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        pos = len(s) - 1
        while(s[pos] == ' '):
            pos -= 1
        
        wordlength = 0
        while pos >= 0 and s[pos] != ' ':
            wordlength += 1
            pos -= 1
        
        return wordlength