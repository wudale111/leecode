'''
找出字符串中第一个只出现一次的字符

数据范围：输入的字符串长度满足 1 \le n \le 1000 \1≤n≤1000

输入描述：
输入一个非空字符串

输出描述：
输出第一个只出现一次的字符，如果不存在输出-1

示例1
输入：
asdfasdfo

复制
输出：
o
'''

while True:
    try:
        str1 = input()
        Flag = False
        for i in str1: #直接按顺序遍历字符串的每一个字符
            if str1.count(i) == 1: #利用内置方法统计其在字符串中的个数
                print(i) #第一次符合只出现一次的条件，则打印出来
                Flag = True # 标记已出现
                break #有找到第一个符合条件的字符后，就退出遍历
        if Flag == False:#遍历完，没有发现符合条件，则打-1
            print(-1)
    except:
        break

# while True:
#     try:
#         a = input()
#         count = -1
#         for i in range(len(a)):
#             if a.count(a[i]) == 1:
#                 count = a[i]
#                 break
#         print(count)
#     except:
#         break