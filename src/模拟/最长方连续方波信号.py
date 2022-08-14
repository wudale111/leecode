while 1:
    try:
        nums = input()

        # 提取信号段，由0分隔的信号段
        dp = []
        cache = []
        for c in nums:
            if cache and cache[-1] == "0" == c:
                dp.append("".join(cache))
                cache = [c]
            else:
                cache.append(c)
        else:
            if cache:
                dp.append("".join(cache))

        # 取不包含11，长度最大的子串
        # 出现了11部分的连续高位，不算完全连续交替方波
        sub = max(dp, key=lambda x: 0 if "11" in x else len(x))
        print(sub)
    except Exception as e:
        break
