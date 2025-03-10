def enhanced_strstr(haystack, needle):
    haystack_len = len(haystack)
    needle_len = len(needle)
 
    for i in range(haystack_len):
        j = 0
        k = i
        match = True
 
        while j < needle_len and k < haystack_len:
            if needle[j] == '[':  # 开始处理可选段
                option_matched = False
                j += 1  # 移动到 '[' 后面的第一个字符
                while needle[j] != ']':
                    if haystack[k] == needle[j]:
                        option_matched = True
                    j += 1  # 移动到下一个可选字符
                if not option_matched:
                    match = False
                    break
                j += 1  # 跳过 ']'
            else:  # 处理普通字符
                if haystack[k] != needle[j]:
                    match = False
                    break
                j += 1  # 移动到 needle 的下一个字符
            k += 1  # 移动到 haystack 的下一个字符
 
        if match:
            return i  # 返回匹配的起始位置
 
    return -1  # 没有匹配
 
if __name__ == "__main__":
    haystack = input().strip()
    needle = input().strip()
    
    result = enhanced_strstr(haystack, needle)
    print(result)