def hex18_to_decimal(hex18_str):
    """将十八进制字符串转换为十进制整数"""
    decimal_value = 0
    for i, char in enumerate(reversed(hex18_str)):
        if char.isdigit():
            value = int(char)
        else:
            value = ord(char.upper()) - ord('A') + 10
        decimal_value += value * (18 ** i)
    return decimal_value

def compare_hex18(hex18_str1, hex18_str2):
    """比较两个十八进制数的大小"""
    decimal1 = hex18_to_decimal(hex18_str1)
    decimal2 = hex18_to_decimal(hex18_str2)
    
    if decimal1 < decimal2:
        return f"{hex18_str1} < {hex18_str2}"
    elif decimal1 > decimal2:
        return f"{hex18_str1} > {hex18_str2}"
    else:
        return f"{hex18_str1} == {hex18_str2}"

# 示例
hex18_num1 = "A3B"
hex18_num2 = "2F1"
result = compare_hex18(hex18_num1, hex18_num2)
print(result)