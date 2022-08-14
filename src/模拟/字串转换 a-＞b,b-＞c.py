def func(c):
    if c == "z":
        return "a"
    else:
        return chr(ord(c)+1)


while 1:
    try:
        nums = input()

        dp = []
        ret = func(nums[0])
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] and i-1 not in dp:
                ret += func(func(nums[i]))
                dp.append(i)
            else:
                ret += func(nums[i])

        print(ret)
    except Exception as e:
        break
