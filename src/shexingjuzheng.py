'''
描述
蛇形矩阵是由1开始的自然数依次排列成的一个矩阵上三角形。
例如，当输入5时，应该输出的三角形为：
1 3 6 10 15
2 5 9 14
4 8 13
7 12
11
输入描述：
输入正整数N（N不大于100）
输出描述：
输出一个N行的蛇形矩阵。
示例1
输入：
4
复制
输出：
1 3 6 10
2 5 9
4 8
7
'''

while 1:
    try:
        num = int(input())
        for i in range(num):
            if i == 0: # 确定第一行的数据
                res = [(x+1)*(x+2)//2 for x in range(num)]
            else: # 剩下的行数只需要在上一行的基础上，从列表下表第一个元素开始减一，即为当前行数据
                res = [x-1 for x in res[1:]]
            print(' '.join(map(str, res))) # 通过使用map 函数将list中的int类型变成string 类型
    except:
        break