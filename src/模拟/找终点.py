while 1:
    try:
        nums = list(map(int, input().split()))

        def dfs(n, c):
            if n == len(nums) - 1:
                return c
            elif n < len(nums):
                return dfs(n+nums[n], c+1)

        dp = []
        for i in range(len(nums)//2):
            t = dfs(i, 1)
            if t:
                dp.append(t)

        if dp:
            print(min(dp))
        else:
            print(-1)
    except Exception as e:
        break
