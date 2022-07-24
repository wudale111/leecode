while 1:
    try:
        num = int(input())

        count = 0
        i = 0
        while i <= num:
            i += 1
            i = int(str(i).replace("4", "5"))
            if i > num:
                break
            count += 1

        print(count)
    except Exception as e:
        break
