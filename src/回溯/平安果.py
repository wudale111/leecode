while 1:
    try:
        m, n = list(map(int, input().split()))

        nums = [list(map(int, input().split())) for _ in range(m)]

        dp = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = nums[i][j]
                elif i == 0:
                    dp[i][j] = dp[i][j-1] + nums[i][j]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + nums[i][j]
                else:
                    dp[i][j] = max((dp[i-1][j], dp[i][j-1])) + nums[i][j]
        print(dp[-1][-1])
    except Exception as e:
        break
