class Solution:
    def intToRoman(self, num: int) -> str:
        nums = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        roman = []
        for a,b in nums:
            while num >= a:
                num = num -a
                roman.append(b)
        return "".join(roman)
'''
创一个字典，然后导入原数字，从大往小减，每减一次，保存减的罗马数字，组成新字符串
'''