while 1:
    try:
        k = int(input())
        nums = input()

        dp = []
        temp = ""
        for c in nums:
            # 按 下换线 双引号 拆分字符串
            # 子串中有同时有 下换线 双引号 的特殊处理
            if c == "_":
                if '"' not in temp and temp:
                    dp.append(temp)
                    temp = ""
                elif '"' in temp:
                    temp += c
            elif c == '"':
                if temp and '"' in temp:
                    temp += c
                    dp.append(temp)
                    temp = ""
                elif temp and '"' not in temp:
                    dp.append(temp)
                    temp = c
                elif not temp:
                    temp = c
            else:
                temp += c
        if temp:
            dp.append(temp)

        # 替换指定下标的 子串为 6个星号
        if k < len(dp):
            nums = nums.replace(dp[k], "*" * 6)
            while "__" in nums:
                nums = nums.replace("__", "_")
            print(nums)
        else:
            print("ERROR")
    except Exception as e:
        break
