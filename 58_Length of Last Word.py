class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        # meet_word = False
        for i in range(len(s)-1, -1, -1): #从末尾开始检测，逐个往前
            ch = ord(s[i]) #转换为ascii编号
            if ch >= 65 and ch <= 122:
                # meet_word = True
                length += 1
            # elif meet_word:
                # break
            if length != 0 and ch < 65 or ch > 122: #检测到遇到第二个空格为止
                break
        return length