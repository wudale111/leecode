while 1:
    try:
        _ = input()

        nums = list(map(int, input().split()))
        min_ = int(input())

        nums = sorted(nums, reverse=True)

        i = 0
        j = len(nums) - 1
        count = 0
        while i < j:
            if nums[i] >= min_:
                count += 1
                i += 1
            elif nums[i] + nums[j] >= min_:
                count += 1
                i += 1
                j -= 1
            else:
                j -= 1

        print(count)
    except Exception as e:
        break
