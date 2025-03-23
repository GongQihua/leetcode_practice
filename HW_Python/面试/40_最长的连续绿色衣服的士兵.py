'''
一队士兵排成一排,身穿绿色跟黑色衣服,如果可以随便将一个士兵移除队伍,那么求最长的连续绿色衣服的士兵队伍长度。
示例:绿色表示1,黑色表示0
输入:
10111
输出:
4
移出第二个位置的黑色士兵,最大连续长度为4.
'''
def longest_green_sequence(soldiers):
    max_length = 0
    n = len(soldiers)
    for i in range(n):
        current_length = 0
        max_current = 0
        for j in range(n):
            if j == i:
                continue
            if soldiers[j] == '1':
                current_length += 1
                max_current = max(max_current, current_length)
            else:
                current_length = 0
        max_length = max(max_length, max_current)
    return max_length

def longest_green_sequence2(soldiers):
    max_length = 0
    left = 0
    zero_count = 0  # 记录窗口中黑色士兵的数量
    
    for right in range(len(soldiers)):
        if soldiers[right] == '0':
            zero_count += 1  # 遇到黑色士兵，增加计数
        
        # 如果窗口中黑色士兵数量超过 1，移动左边界
        while zero_count > 1:
            if soldiers[left] == '0':
                zero_count -= 1
            left += 1
        
        # 更新最大长度
        max_length = max(max_length, right - left)
    
    return max_length

soldiers = "101111"
print(longest_green_sequence(soldiers))  # 4
print(longest_green_sequence2(soldiers))  # 4