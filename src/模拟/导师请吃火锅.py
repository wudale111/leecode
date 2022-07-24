while 1:
    try:
        n, m = list(map(int, input().split()))

        idx = []
        for _ in range(n):
            i, v = list(map(int, input().split()))
            idx.append(i+v)

        nums = [0] * (max(idx)+1)
        for i in idx:
            nums[i] = 1

        dp = []

        def dfs(t, data):
            # t 可以夹菜的时间, 因为每秒夹一次，也可作为时间轴
            if t >= len(nums):
                dp.append(sum(data))
                return
            # 等于 1 此时有菜，但是可以选择吃或者不吃，可能会影响后面夹菜的顺序
            if nums[t] == 1:
                # 1 表示吃，吃了要直接跳到m秒后
                # 没吃 过1s继续选择 吃或者不吃
                dfs(t+m, data + [1])
                dfs(t+1, data)
            else:
                dfs(t+1, data)

        dfs(1, [])

        print(max(dp))
    except Exception as e:
        break
