"""
最终dp的值
dp = [[1, 1, 1, 0, 0, 0],
      [1, 1, 2, 1, 1, 1],
      [1, 1, 2, 1, 1, 1],
      [1, 2, 3, 2, 2, 1],
      [1, 2, 3, 2, 2, 1],
      [1, 2, 2, 1, 1, 0],
      [1, 1, 1, 0, 0, 0]
      ]

"""
while 1:
    try:
        xs = []
        ys = []

        nums = []
        for _ in range(3):
            x1, y1, w, h = list(map(int, input().split()))
            # x1, y1 左上角
            # x2, y2 右上角
            x2 = x1 + w
            y2 = y1 - h
            xs += [x1, x2]
            ys += [y1, y2]
            # 记录矩形坐标
            nums.append((x1, y1, x2, y2))

        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)

        # 坐标轴偏移量
        x = 0 - min_x
        y = 0 - min_y
        # 构建二维数据
        dp = [[0] * abs(max_y-min_y) for _ in range(abs(max_x-min_x))]

        for x1, y1, x2, y2 in nums:
            # 需要 转成 二维数组的下标
            for i in range(min((x2, x1)) + x, max((x2, x1)) + x):
                for j in range(min((y2, y1)) + y, max((y2, y1)) + y):
                    # 绘制矩形，最终的数值表示被矩形覆盖的次数
                    dp[i][j] += 1

        ret = 0
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                # 数值为3，是三个矩形的交集
                if dp[i][j] == 3:
                    ret += 1
        print(ret)
    except Exception as e:
        break
