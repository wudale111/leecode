dct = {
    "1": ',.',
    "2": 'abc',
    "3": 'def',
    "4": 'ghi',
    "5": 'jkl',
    "6": 'mno',
    "7": 'pqrs',
    "8": 'tuv',
    "9": 'wxyz',
}


def func(nums):
    if nums and nums[0] in dct:
        que = dct[nums[0]]
        return que[len(nums) % len(que)-1]
    else:
        return nums


while 1:
    try:
        nums = input()

        # True 数字
        # False 拼音
        flg = True

        ret = ""
        bef = ""
        for c in nums:
            if c == "#":
                flg = not flg
                ret += func(bef)
                bef = ""
            elif flg:
                ret += func(bef)
                bef = ""
                ret += c
            else:
                if c == "/":
                    ret += func(bef)
                    bef = ""
                elif bef and c == bef[-1]:
                    bef += c
                else:
                    ret += func(bef)
                    bef = c
        if bef:
            ret += func(bef)

        print(ret)
    except Exception as e:
        break
