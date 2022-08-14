while 1:
    try:
        n, m = list(map(int, input().split()))

        nums = []
        for _ in range(m):
            tmp = input().split()
            a = int(tmp[0])
            b = int(tmp[1])
            com = tmp[2]
            nums.append((a, b, com))

        dp = []
        for a, b, com in nums:
            if not (1 <= a <= n and 1 <= b <= n):
                print("da pian zi")
                continue
            if com == "0":
                if dp:
                    for idx, val in enumerate(dp):
                        if val.intersection({a, b}):
                            dp[idx] = val.union({a, b})
                            break
                    else:
                        dp.append({a, b})
                else:
                    dp.append({a, b})
            elif com == "1":
                for i in dp:
                    if i.intersection({a, b}) == {a, b}:
                        print("we are a team")
                        break
                else:
                    print("we are not a team")
            else:
                print("da pian zi")
    except Exception as e:
        break
