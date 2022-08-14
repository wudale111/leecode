while 1:
    try:
        nums = input().split(',')

        def dfs(ids, max_, dp):
            sub = "".join([nums[i] for i in ids])
            if 0 <= int(sub) < max_ and len(sub) == 2:
                dp.append((sub, ids))
            else:
                for i in range(len(nums)):
                    if i not in ids:
                        dfs(ids+[i], max_, dp)

        def fun(max_):
            dp = []
            for i in range(len(nums)):
                dfs([i], max_, dp)
            dp = sorted(dp, key=lambda x: int(x[0]), reverse=True)
            if dp:
                for c in str(dp[0][0]):
                    nums.remove(c)
                return str(dp[0][0])

        # 取最大小时数
        h = fun(24)
        # 取最大分钟数
        m = fun(60)
        # 取最大秒数
        s = fun(60)

        if h and m and s:
            print(f"{h}:{m}:{s}")
        else:
            print("ivalid")

    except Exception as e:
        break
