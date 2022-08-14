while 1:
    try:
        n = int(input())
        ids = input().split(',')
        nums = list(map(int, input().split(',')))

        dct = {}
		# 关联用户和成绩
        for i in range(n):
            id_ = ids[i]
            if id_ in dct:
                dct[id_].append(nums[i])
            else:
                dct[id_] = [nums[i]]

        dp = []
        # 剔除成绩少于三个的用户，并只保留最高三次成绩
        for k, v in dct.items():
            if len(v) >= 3:
                dp.append((k, sorted(v, reverse=True)[:3]))

		# 按最高三次成绩和排序
        dp = sorted(dp, key=lambda x: sum(x[1]), reverse=True)
        print(",".join([k for k, v in dp]))
    except Exception as e:
        break
