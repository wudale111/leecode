while 1:
    try:
        nums = list(map(int, input().split()))
        k = int(input())

        for i in range(len(nums)):
            if nums[i] < k:
                nums[i] = 1
            else:
                nums[i] = 0

        n = len(nums)
        m = sum(nums)

        dp = []
        for i in range(n):
            dp.append(sum(nums[i: i+m]))

        print(m-max(dp))
    except Exception as e:
        break
