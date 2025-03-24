# 实现超级长的数字减1的功能
def minus_one(s: str) -> str:
    num_str = s.strip()
    if num_str[0] == '-':
        num_str = num_str[1:]
        result = plus_one(num_str)
        return '-' + result
    
    if num_str == '0':
        return '-1'
    
    num_list = list(num_str)
    i = len(num_list) - 1
    while i >= 0:
        if num_list[i] == '0':
            num_list[i] = '9'
            i -= 1
        else:
            num_list[i] = str(int(num_list[i]) - 1)
            break
    result = ''.join(num_list).lstrip('0')
    if result == '':
        return '0'
    return result

def plus_one(s: str) -> str:
    num_list = list(s)
    carry = 1
    i = len(num_list) - 1

    while i >= 0 and carry:
        temp = int(num_list[i]) + carry
        num_list[i] = str(temp % 10)
        carry = temp // 10
        i -= 1

    if carry:
        num_list.insert(0, '1')
    
    return ''.join(num_list)

print(minus_one("123456789012345678901234567890"))  # 正常大数
print(minus_one("1000"))                            # 有借位
print(minus_one("1"))                               # 直接变0
print(minus_one("0"))                               # 特殊，变-1
print(minus_one("-1000"))                           # 负数减一
print(minus_one("-1"))                             # 负数减一