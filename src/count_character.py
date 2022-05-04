def count_character(str):
    string = ''.join(set(str))  # 去重后以字符串的形式
    count = 0  # 开始计数
    for item in string:
        if 0 <= ord(item) <= 127:  # ASCII码范围要求
            count += 1  # 计数
    return count


str = input()
print(count_character(str))