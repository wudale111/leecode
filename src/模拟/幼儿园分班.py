
while 1:
    try:
        nums = input().split()

        # 第一个同学
        start = nums[0].split('/')
        A = [start[0]]
        B = []

        temp = [A, B]  # 表示前一个同学的班级， 默认是 A 班级
        # 从第二个同学开始判断
        for n in nums[1:]:
            id_, f = n.split("/")

            if f == "Y":
                temp = temp
            else:
                # 不在一个班，需要交换班级顺序
                temp = temp[::-1]

            temp[0].append(id_)

        if A:
            print("".join(sorted(A, key=lambda x: int(x))))
        if B:
            print("".join(sorted(B, key=lambda x: int(x))))
    except Exception as e:
        print(traceback.print_exc())
        break
