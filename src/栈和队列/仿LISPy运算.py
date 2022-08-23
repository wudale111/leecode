while 1:
    try:
        nums = input().split()
        stack_a = []
        stack_b = []

        for c in nums:
            if "(" in c:
                stack_a.append("(")
                stack_a.append(c[1:])
            elif ")" in c:
                stack_a.append(c[:c.index(")")])
                stack_a += list(c[c.index(")"):])
            else:
                stack_a.append(c)

        while stack_a:
            temp = stack_a.pop()
            if temp == ")":
                stack_b.append(temp)
            elif temp == "(":
                com = stack_b.pop()
                # add / sub / mul / div
                a = int(stack_b.pop())
                b = int(stack_b.pop())
                # 当前计算公式的右括号
                stack_b.pop()
                if com == "add":
                    stack_b.append(a+b)
                elif com == "sub":
                    stack_b.append(a-b)
                elif com == "mul":
                    stack_b.append(a*b)
                else:
                    if b == 0:
                        print("error")
                        break
                    stack_b.append(a//b)
            else:
                stack_b.append(temp)

        if stack_b:
            print(stack_b.pop())
    except Exception as e:
        break
