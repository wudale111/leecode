while 1:
    try:
        x, y = map(int, input().split())

        dp = [["#"] * y for _ in range(x)]

        # 构造迷宫
        for _ in range(int(input())):
            i, j = map(int, input().split())
            dp[i][j] = 0

        def dfs(x_, y_):
            # 到达终点
            if x_ == x - 1 and y_ == y - 1:
                dp[x_][y_] = 1
                return 1
            # 到达边界或障碍物
            elif x_ > x - 1 or y_ > y - 1 or dp[x_][y_] == 0:
                return -1
            else:
                # 更新可以到达的格子
                dp[x_][y_] = max(dfs(x_ + 1, y_), dfs(x_, y_ + 1))
                return dp[x_][y_]
		# 从 0,0 点出发
        dfs(0, 0)

        c1 = 0
        c2 = 0
        for line in dp:
            c1 += line.count(-1)
            c2 += line.count("#")
        print(c1, c2)
    except Exception as e:
        break

