while 1:
    try:
        hh, mm = input().split(":")

        chars = set(list(hh) + list(mm))
        hhmm = hh+mm

        dp = []

        def dfs(hm_):
            lens = len(hm_)
            if lens == 2 and hm_ > "23":
                return
            elif lens == 3 and (hm_ > "235" or hm_[2] > "5"):
                return
            elif lens >= 4:
                if hm_ > hhmm:
                    dp.append(hm_)

                else:
                    dp.append("1"+hm_)
                print(dp)
            else:
                for c in chars:
                    dfs(hm_+c)

        for c in chars:
            if c <= "2":
                dfs(c)

        ret = sorted(dp, key=lambda x: int(x))[0]
        if len(ret) == 5:
            print(f"{ret[1:3]}:{ret[3:]}")
        else:
            print(f"{ret[:2]}:{ret[2:]}")
    except Exception as e:
        break
