import re

def solve(info):
    # 使用正则表达式提取所有形如 (x,y) 的坐标对
    pattern = re.compile(r'\((\d+),(\d+)\)')
    matches = pattern.findall(info)
    
    max_dis = 0
    max_index = "(0,0)"
    
    for x_str, y_str in matches:
        # 检查 x 和 y 是否以 0 开头
        if x_str.startswith('0') or y_str.startswith('0'):
            continue
        
        x = int(x_str)
        y = int(y_str)
        
        # 检查 x 和 y 是否在 (0, 1000) 范围内
        if 0 < x < 1000 and 0 < y < 1000:
            dis = x ** 2 + y ** 2
            if dis > max_dis:
                max_dis = dis
                max_index = f"({x},{y})"
    
    return max_index

# 测试
print(solve(input()))