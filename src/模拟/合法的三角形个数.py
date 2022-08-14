while 1:
    try:
        nums = list(map(int, input().split()))
        nums = sorted(nums)
        lens = len(nums)

        # [left, right] 窗口内的数和 [i] 始终满足三角形
        count = 0
        for i in range(lens):
            left = i + 1
            right = i + 2
            while left < lens:
                while right < lens and nums[right] < nums[i] + nums[left]:
                    count += max(right - left, 0)
                    right += 1
                left += 1
        print(count)
    except Exception:
        break


while 1:
    try:
        nums = list(map(int, input().split()))
        nums = sorted(nums)
        lens = len(nums)
        count = 0
        for i in range(lens-2):
            for j in range(i + 1, lens-1):
                for k in range(j + 1, lens):
                    a = nums[i]
                    b = nums[j]
                    c = nums[k]
                    # 任意两条边之和要大于第三边
                    if a + b > c:
                        count += 1
        print(count)
    except Exception:
        break
