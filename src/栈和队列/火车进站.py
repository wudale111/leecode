'''
描述
给定一个正整数N代表火车数量，0<N<10，接下来输入火车入站的序列，一共N辆火车，每辆火车以数字1-9编号，火车站只有一个方向进出，同时停靠在火车站的列车中，只有后进站的出站了，先进站的才能出站。
要求输出所有火车出站的方案，以字典序排序输出。
数据范围：1\le n\le 10\1≤n≤10
进阶：时间复杂度：O(n!)\O(n!) ，空间复杂度：O(n)\O(n)
输入描述：
第一行输入一个正整数N（0 < N <= 10），第二行包括N个正整数，范围为1到10。

输出描述：
输出以字典序从小到大排序的火车出站序列号，每个编号以空格隔开，每个输出序列换行，具体见sample。

示例1
输入：
3
1 2 3
复制
输出：
1 2 3
1 3 2
2 1 3
2 3 1
3 2 1
复制
说明：
第一种方案：1进、1出、2进、2出、3进、3出
第二种方案：1进、1出、2进、3进、3出、2出
第三种方案：1进、2进、2出、1出、3进、3出
第四种方案：1进、2进、2出、3进、3出、1出
第五种方案：1进、2进、3进、3出、2出、1出
请注意，[3,1,2]这个序列是不可能实现的。
'''

# while True:
#     try:
#         n = int(input())
#         trains = input().strip().split(' ')
#         res = []
#         def rec_trains(cur_idx, in_trains, out_trains):
#             # 如果原始火车列表的最后一个元素已经进站，此时只能出站，将入站列表中的火车倒序加入出站火车中
#             if trains[-1] in in_trains:
#                 res.append(' '.join(out_trains + in_trains[::-1]))
#                 return
#             # 如果进站列表为空，此时只能进站，进站列表加上当前火车，出站列表不变
#             elif in_trains == []:
#                 rec_trains(cur_idx + 1, in_trains + [trains[cur_idx]], out_trains)
#             # 否则，就既有可能进站也有可能出站
#             else:
#                 # 出站，当前火车索引不变，进站火车列表减去最后一个元素，出站列表加上进站列表刚刚出站的火车
#                 rec_trains(cur_idx, in_trains[:-1], out_trains + [in_trains[-1]])
#                 # 进站，当前火车索引加1，进站列表加上当前火车，出站列表不变
#                 rec_trains(cur_idx + 1, in_trains + [trains[cur_idx]], out_trains)
#         rec_trains(0, [], [])
#         res.sort()
#         print('\n'.join(res))
#     except:
#         break
a=1
b=2
c=3
d=4
if a==1:
    print(a)

elif b== 2:
    print(b)
else:
    print(c)




# res = []
# def dfs(wait, stack, out):
#     if not wait and not stack:
#         res.append(' '.join(map(str, out)))
#     if wait:  # 入栈
#         dfs(wait[1:], stack + [wait[0]], out)
#     if stack:  # 出栈
#         dfs(wait, stack[:-1], out + [stack[-1]])
#
#
# while True:
#     try:
#         n, nums = int(input()), list(map(int, input().split()))
#         dfs(nums, [], [])
#         for i in sorted(res):
#             print(i)
#     except:
#         break