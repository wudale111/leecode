while 1:
    try:
        nums = list(map(int, input().split(',')))
        dp = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                dp[i] = max(dp[i], (j - i) * min((nums[i], nums[j])))
        print(max(dp))
    except Exception as e:
        break
