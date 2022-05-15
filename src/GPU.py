'''
         为了充分发挥Gpu算力，
         需要尽可能多的将任务交给GPU执行，
         现在有一个任务数组，
         数组元素表示在这1s内新增的任务个数，
         且每秒都有新增任务，
         假设GPU最多一次执行n个任务，
         一次执行耗时1s，
         在保证Gpu不空闲的情况下，最少需要多长时间执行完成。

         输入描述
           第一个参数为gpu最多执行的任务个数
           取值范围1~10000
           第二个参数为任务数组的长度
           取值范围1~10000
           第三个参数为任务数组
           数字范围1~10000

'''
# n =int(input())
# len = int(input())
# ints = list(map(int,input().split()))
#
# time =0
# more=0
# for i in ints:
#     if i +more >n:
#         more= i+more -n
#     else:
#         more =0
#     print(more)
#     time +=1
# while more >0:
#     more -=n
#     time +=1
# print(time)

n = int(input())
len = int(input())
ints = list(map(int,input().split()))

time = 0
more = 0
for i in ints:
    if i-more >n:
        more= i-n+more
    else:
        more = 0
    time +=1

while(more>n):
    more = more -n
    time +=1
print(time)