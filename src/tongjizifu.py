'''
描述
输入一行字符，分别统计出包含英文字母、空格、数字和其它字符的个数。

数据范围：输入的字符串长度满足 1 \le n \le 1000 \1≤n≤1000

输入描述：
输入一行字符串，可以有空格

输出描述：
统计其中英文字符，空格字符，数字字符，其他字符的个数
'''

str = input()
alp_time =0
space_time =0
digital_time = 0
other_time = 0
for i in str:
    if i.isalpha():
        alp_time +=1
    elif i.isdigit():
        digital_time +=1
    elif i.isspace():
        space_time +=1
    else:
        other_time +=1

print(alp_time)
print(digital_time)
print(space_time)
print(other_time)