while 1:
    try:
        n, m = map(int, input().split())

        map_ = [input().split() for i in range(m)]
        # 小华小为的坐标
        start_spots = []
        # 聚餐点坐标
        end_spots = []

        for i in range(m):
            for j in range(n):
                if map_[i][j] == "2":
                    start_spots.append((i, j))
                elif map_[i][j] == "3":
                    end_spots.append((i, j))

        count = 0
        for end_ in end_spots:

            def dfs(si, sj, cache):
                if (si, sj) in cache:
                    return False
                cache.append((si, sj))
                # 控制地图边界
                if not (0 <= si < m and 0 <= sj < n):
                    return False
                # 遇到障碍物
                if map_[si][sj] == "1":
                    return False
                if (si, sj) == tuple(end_):
                    return True

                # 有四种情况可以向上下左右走
                return dfs(si+1, sj, cache) or dfs(si-1, sj, cache) \
                       or dfs(si, sj+1, cache) or dfs(si, sj-1, cache)

            # 已到达的坐标，避免重复计算
            cache_a = []
            cache_b = []
            if dfs(start_spots[0][0], start_spots[0][1], cache_a) \
                    and dfs(start_spots[1][0], start_spots[1][1], cache_b):
                count += 1

        print(count)
    except Exception as e:
        break
