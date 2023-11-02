class Solution:
    VALUE_SYMBOLS = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]
    def intToRoman(self, num: int) -> str:
        roman = []
        for value, symbol in Solution.VALUE_SYMBOLS:
            while num >= value:
                num -= value
                roman.append(symbol)
            if num == 0:
                break
        return ''.join(roman)
'''
创一个字典，然后导入原数字，从大往小减，每减一次，保存减的罗马数字，组成新字符串
因为4和9的特殊性，记得直接把4，9，40，90，400，900的情况写进dic里
'''