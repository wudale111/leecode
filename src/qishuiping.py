'''
某商店规定：三个空汽水瓶可以换一瓶汽水，允许向老板借空汽水瓶（但是必须要归还）。
小张手上有n个空汽水瓶，她想知道自己最多可以喝到多少瓶汽水。
数据范围：输入的正整数满足 1 \le n \le 100 \1≤n≤100

注意：本题存在多组输入。输入的 0 表示输入结束，并不用输出结果。
输入描述：
输入文件最多包含 10 组测试数据，每个数据占一行，仅包含一个正整数 n（ 1<=n<=100 ），表示小张手上的空汽水瓶数。n=0 表示输入结束，你的程序不应当处理这一行。

输出描述：
对于每组测试数据，输出一行，表示最多可以喝的汽水瓶数。如果一瓶也喝不到，输出0。
输入：
3
10
81
0
输出：
1
5
40
'''
# kongping =10
# qishui = 0
# while kongping >=2:
#     if kongping >2:
#         qishui =kongping //3
#         endkongping = kongping % 3
#         qishui =endkongping+ qishui % 3
#         kongping = + qishui // 3
#     else:
#         qishui +=1
#         kongping =0
# print(qishui)


def func():
    while True:
        try:
            n = input().strip()
            n = int(n)
            res = 0
            if n > 0:
                a = n
                while a >= 2:
                    if a > 2:
                        b = a // 3
                        res += b
                        a = b + a % 3
                    else:
                        res += 1
                        a = 0
                print(res)

        except:
            break


if __name__ == "__main__":
    func()