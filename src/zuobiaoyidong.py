'''
描述
开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。从（0,0）点开始移动，从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。

输入：

合法坐标为A(或者D或者W或者S) + 数字（两位以内）
'''
str =input()
strlist = str.split(';')
x,y=0,0
for i in strlist:
    #按字母和数字能分开？
    if 'A' in i:
        x -=10

# input_list = input().split(';')
# initial = [0, 0]
# for item in input_list:
#     if not 2 <= len(item) <= 3:
#         continue
#
#     try:
#         direction = item[0]
#         step = int(item[1:])
#         if direction in ['A', 'D', 'W', 'S']:
#             if 0 <= step <= 99:
#                 if direction == 'A':
#                     initial[0] -= step
#                 elif direction == 'D':
#                     initial[0] += step
#                 elif direction == 'S':
#                     initial[1] -= step
#                 elif direction == 'W':
#                     initial[1] += step
#     except:
#         continue
#
# print(str(initial[0]) + ',' + str(initial[1]))