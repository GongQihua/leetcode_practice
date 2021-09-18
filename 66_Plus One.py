class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1 , -1): #从末位开始检测
            digits[i] += 1
            digits[i] %= 10 #逢10进位的方法
            if digits[i] != 0:
                return digits #遇第二个数停止
        return [1] + digits #防止进位后没首位