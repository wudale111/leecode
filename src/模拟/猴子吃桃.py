while 1:
    try:
        *nums, h = list(map(int, input().split()))

        if len(nums) > h:
            print(-1)
        else:
            for i in range(1, max(nums)+1):
                if sum([int(n/i+0.5) for n in nums]) <= h:
                    print(i)
                    break
            else:
                print(-1)

    except Exception as e:
        break
