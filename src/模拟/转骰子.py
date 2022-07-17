while 1:
    try:

        nums = "123456"
        comm = input()
        for c in comm:
            if c == "L":
                nums = f"{nums[4:]}{nums[2:4]}{nums[:2][::-1]}"
            elif c == "R":
                nums = f"{nums[4:][::-1]}{nums[2:4]}{nums[:2]}"
            elif c == "F":
                nums = f"{nums[:2]}{nums[4:]}{nums[2:4][::-1]}"
            elif c == "B":
                nums = f"{nums[:2]}{nums[4:][::-1]}{nums[2:4]}"
            elif c == "A":
                nums = f"{nums[2:4][::-1]}{nums[:2]}{nums[4:]}"
            else:
                nums = f"{nums[2:4]}{nums[:2][::-1]}{nums[4:]}"
        print(nums)

    except Exception as e:
        break
