while 1:
    try:
        logs = []
        dp = None
        while 1:
            log = input().split(',')
            if len(log) == 3:
                logs.append(list(map(int, log)))
            else:
                dp = [0] * int(log[0])
                break

        for i, j, k in logs:
            for i_ in range(i-1, j):
                dp[i_] += k

        print(",".join(list(map(str, dp))))
    except Exception as e:
        break
