while 1:
    try:
        n = int(input())
        nums = list(map(int, input().split(",")))

        def funcl(i, w):
            if w > 0 and i >= 0:
                nums[i] = max(nums[i], w)
                funcl(i - 1, w - 100)

        def funcr(i, w):
            if w > 0 and i < n-1:
                nums[i] = max(nums[i], w)
                funcr(i + 1, w - 100)

        for i in range(n):
            funcl(i-1, nums[i]-100)
            funcr(i, nums[i])

        ret = 0
        r = nums[0]
        for l in nums[1:]:
            ret += 100 - min(100, r+l)
            r = l
        print(ret)
    except Exception as e:
        break
