while 1:
    try:
        n = int(input())

        nums = [input().split() for _ in range(n)]

        print(nums)
        nums = sorted(
            nums,
            key=lambda x: (int(x[1]), int(x[2]), int(x[3]), x[0]),
            reverse=True
        )

        for i in nums:
            print(i[0])
    except Exception as e:
        break
