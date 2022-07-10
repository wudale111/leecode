'''
 * 标题：字符串分割 | 时间限制：1秒 | 内存限制：262144K | 语言限制：不限
 * 给定一个非空字符串S，其被N个‘-’分隔成N+1的子串，给定正整数K，要求除第一个子串外，其余的子串每K个字符组成新的子串，并用‘-’分隔。
 * 对于新组成的每一个子串，如果它含有的小写字母比大写字母多，则将这个子串的所有大写字母转换为小写字母；
 * 反之，如果它含有的大写字母比小写字母多，则将这个子串的所有小写字母转换为大写字母；大小写字母的数量相等时，不做转换。
 * <p>
 * 输入为两行，第一行为参数K，第二行为字符串S。
 * 输出描述:
 * 输出转换后的字符串。
 * <p>
 * 示例1
 * 输入
 * 3
 * 12abc-abCABc-4aB@
 * 输出
 * 12abc-abc-ABC-4aB-@
 * 说明
 * 子串为12abc、abCABc、4aB@，第一个子串保留，后面的子串每3个字符一组为abC、ABc、4aB、@，
 * abC中小写字母较多，转换为abc，ABc中大写字母较多，转换为ABC，4aB中大小写字母都为1个，不做转换，@中没有字母，连起来即12abc-abc-ABC-4aB-@
 * <p>
 * 示例2
 * 输入
 * 12
 * 12abc-abCABc-4aB@
 * 输出
 * 12abc-abCABc4aB@
 * 说明
 * 子串为12abc、abCABc、4aB@，第一个子串保留，后面的子串每12个字符一组为abCABc4aB@，这个子串中大小写字母都为4个，不做转换，连起来即12abc-abCABc4aB@
'''
while 1:
    try:
        k = int(input())
        head, tail = input().split("-", 1)

        tail = tail.replace("-", "")
        temp = ""
        for index in range(0, len(tail), k):
            line = tail[index: index + k]
            count1 = 0
            count2 = 0
            for c in line:
                if "A" <= c <= "Z":
                    count1 += 1
                if "a" <= c <= "z":
                    count2 += 1
            if count1 == count2:
                temp += line
            elif count1 > count2:
                temp += line.upper()
            else:
                temp += line.lower()

            # 按长度k分隔处理后的字符串
        dp = []
        for index in range(0, len(temp), k):
            dp.append(temp[index: index + k])

        print(f"{head}-{'-'.join(dp)}")

        # 推导式写法
        # print(f"{head}-{'-'.join([temp[index: index+k] for index in range(0, len(temp), k)])}")
    except Exception as e:
        break
