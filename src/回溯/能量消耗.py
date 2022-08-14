while 1:
    try:
        n = int(input())
        nums = [list(map(int, input().split())) for _ in range(n)]

        def dfs(idx, com, val):
            # idx 用户id
            # com 三个策略
            # val 资源消耗
            if idx == n - 1:
                return val
            idx += 1
            return max([dfs(idx, c, nums[idx][c]) + val for c in [0, 1, 2] if c != com])

        dp = []
        for c in [0, 1, 2]:
            dp.append(dfs(0, c, nums[0][c]))

        print(max(dp))
    except Exception as e:
        break

