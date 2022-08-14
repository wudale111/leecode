while 1:
    try:
        nums = input().replace(" ", "").split(',')
        n = int(input())

        dp = []
        lens = len(nums)

        def dfs(sub):
            if len(sub) >= lens:
                dp.append(sub)
                return

            if len(sub) >= n:
                dp.append(sub)

            for c in nums:
                if c not in sub and sub[-1] < c:
                    dfs(sub+c)

        for c in nums:
            dfs(c)

        for w in dp:
            print(w)
    except Exception as e:
        break
