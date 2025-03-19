def enhance_strstr(haystack, needle):
    haystack_len = len(haystack)
    needle_len = len(needle)

    for i in range(haystack_len):
        j = 0
        k = i
        match = True

        while j < needle_len and k < haystack_len:
            if needle[j] == '[':
                option_matched = False
                j += 1
                while needle[j] != ']':
                    if haystack[k] == needle[j]:
                        option_matched = True
                    j += 1
                if not option_matched:
                    match = False
                    break
                j += 1
            else:
                if haystack[k] != needle[j]:
                    match = False
                    break
                j += 1
            k += 1

        if match:
            return i
        
    return -1

if __name__ == '__main__':
    haystack = input().strip()
    needle = input().strip()
    result = enhance_strstr(haystack, needle)
    print(result)