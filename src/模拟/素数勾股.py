def ac(a, b):
    # 返回最大公约数
    mod = 2  # 随便定义一个余数
    while mod != 0:  # 当余数等于0是最大公约数
        mod = a % b
        a = b
        b = mod
    return a


while 1:
    try:
        m = int(input())

        dp = []
        for a in range(m + 1):
            for b in range(a + 1, m + 1):
                for c in range(b + 1, m + 1):
                    # 互质 最大公约数为1
                    if a * a + b * b == c * c and ac(a, b) == ac(b, c) == ac(a, c) == 1:
                        dp.append((a, b, c))
        print(len(dp))
    except Exception as e:
        break
