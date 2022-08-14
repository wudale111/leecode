def fun(num):
    # 判断是否是一个有效的水仙花数
    a, b, c = list(map(int, list(str(num))))
    return a**3 + b**3 + c**3 == num


while 1:
    try:
        base = input()
        nums = [ord(c) for c in base]

        i = 0
        j = 1

        dp = []

        def dfs(inums, subs):
            i = 0
            j = 1
            while j <= len(inums):
                total = sum(inums[i: j])
                # 水仙花数 是一个3位数，在 100 到 1000 之间
                if total < 100:
                    j += 1
                elif total < 1000:
                    if fun(total):
                        dfs(inums[j:], subs+["".join([chr(n) for n in inums[i: j]])])
                    j += 1
                else:
                    break
            else:
                if "".join(subs) == base:
                    dp.append(subs)

        dfs(nums, [])

        if not dp:
            print(0)
        elif len(dp) == 1:
            print(len(dp[0]))
        else:
            print(-1)
    except Exception as e:
        break
