while 1:
    try:
        nums = list(map(int, input().split(",")))

        dct = {}
        for c in nums:
            if c in dct:
                dct[c] += 1
            else:
                dct[c] = 1
        if len(set(dct.values())) == 1:
            count = max(dct.values())
            keys = sorted(dct.keys())

            for i in keys:
                print(",".join([str(i)]*count))
        else:
            print(-1)

    except Exception as e:
        break
