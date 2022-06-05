'''
描述
输入n个整数，找出其中最小的k个整数并按升序输出

本题有多组输入样例

数据范围：1 \le n \le 1000 \1≤n≤1000  ，输入的整数满足 1 \le val \le 10000 \1≤val≤10000
输入描述：
第一行输入两个整数n和k
第二行输入一个整数数组

输出描述：
从小到大输出最小的k个整数，用空格分开。

示例1
输入：
5 2
1 3 5 7 2
复制
输出：
1 2
'''

# n,k=map(int,input().split())
# str1=input().split()
# list1 = []
# for i in str1:
#     list1.append(int(i))
# list1.sort()
# for i in range(k):
#     print(list1[i],end=(' '))
#map不能用sort,是个内存值，能遍历，能用list
n,k = list(map(int,input().split()))
num = list(map(int,input().split()))
num = sorted(num)
for i in num[:k]:
    print(i,end=' ')