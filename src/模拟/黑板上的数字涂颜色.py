while 1:
    try:
        _ = input()
        nums = list(map(int, input().split()))

        dp = []
        while nums:
            # 取最小值 并将最小值的倍数 分为一组
            min_ = min(nums)
            ca = []
            i = 0
            while i < len(nums):
                if nums[i] % min_ == 0:
                    ca.append(nums[i])
                    nums.pop(i)
                else:
                    i += 1
            dp.append(ca)

        print(len(dp))
    except Exception as e:
        break
