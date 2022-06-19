'''
把m个同样的苹果放在n个同样的盘子里，允许有的盘子空着不放，问共有多少种不同的分法？
注意：如果有7个苹果和3个盘子，（5，1，1）和（1，5，1）被视为是同一种分法。

数据范围：0 \le m \le 10 \0≤m≤10 ，1 \le n \le 10 \1≤n≤10 。

输入描述：
输入两个int整数

输出描述：
输出结果，int型

示例1
输入：
7 3
复制
输出：
8
'''

# def solution(m,n):
#     if m == 0 or m == 1 or n == 1:                  # 如果没有苹果了或只有1个苹果，则方案数返回1；如果只有一个盘子了，剩下的苹果必须全放盘子里，因此也只剩下一种方案
#         return 1
#     if m<n:
#         return solution(m,m)
#     if m>n:
#         return solution(m,n-1)+solution(m-n,n)


def solution(m, n):
    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(m + 1):
        dp[i][1] = 1  # 如果只有一个盘子则只有一种放置方案
    for j in range(1, n + 1):
        dp[0][j] = 1  # 如果没有苹果则只有一种放置方案
        dp[1][j] = 1  # 如果只有一个苹果也相当于只有一种方案
    for i in range(2, m + 1):
        for j in range(2, n + 1):
            if i < j:  # 如果苹果数量少，则盘子一定会空，所以去除那些空的盘子其实不影响方案数
                dp[i][j] = dp[i][i]
            else:  # 如果苹果数量多，则考虑是否要装够j个盘子，如果不装够则有dp[i][j-1]，如果装够则相当于从所有盘子同时去掉一个苹果无影响，则有dp[i-j][j]
                dp[i][j] = dp[i - j][j] + dp[i][j - 1]

    return dp[m][n]


while True:
    try:
        m, n = map(int, input().split())
        print(solution(m, n))
    except:
        break