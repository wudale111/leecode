'''
输入一个 int 型的正整数，计算出该 int 型数据在内存中存储时 1 的个数。

数据范围：保证在 32 位整型数字范围内
输入描述：
 输入一个整数（int类型）
输出描述：
 这个数转换成2进制后，输出1的个数
示例1
输入：
5
输出：
2
'''

number = int(input())
n=0
list = []
while number >=1:
    yushu = number % 2
    list.append(yushu)
    number = number //2

for i in list:
    if i == 1:
        n +=1
print(n)
