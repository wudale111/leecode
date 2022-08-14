while 1:
    try:
        nums = list(map(int, input().split()))

        dct = {}
        for c in nums:
            if c in dct:
                dct[c] += 1
            else:
                dct[c] = 1

        ret = []
        for k, v in dct.items():
            if v == 1:
                ret.append(str(k))

        print(" ".join(ret))
    except Exception as e:
        break
