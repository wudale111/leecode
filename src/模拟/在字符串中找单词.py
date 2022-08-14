while 1:
    try:
        nums = input()+"#"

        dp = []

        temp = ""
        for c in nums:
            if "a" <= c <= "z" or "A" <= c <= "Z":
                temp += c
            else:
                if len(temp) > 1 and temp not in dp:
                    dp.append(temp)
                temp = ""
        dp = sorted(dp, key=lambda x: len(x), reverse=True)
        print(" ".join(dp))
    except Exception as e:
        break
