while 1:
    try:
        # 人员总数
        n = int(input())
        # 第k个人开始
        k = int(input())
        # 每m个人出列
        m = int(input())

        # 构建圆桌
        nums = list(range(1, n + 1))

        # 移动队头，确保从第k个人开始
        nums = nums[k - 1:] + nums[:k - 1]
        dp = []

        while len(nums) >= m:
            # 记录需要移出的人员
            cache = list(range(m - 1, len(nums), m))
            nums_ = []
            for i in range(len(nums)):
                if i in cache:
                    # 将移出的人更新至dp
                    dp.append(nums[i])
                elif i > cache[-1]:
                    # 重新构建圆桌
                    nums = nums[i:] + nums_
                    break
                else:
                    nums_.append(nums[i])
            else:
                nums = nums_

        print(dp[-1])
    except Exception as e:
        break
