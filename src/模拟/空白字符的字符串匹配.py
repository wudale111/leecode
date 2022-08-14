while 1:
    try:
        nums = input().replace(" ", "").replace("\t", "")
        sub = input()

        count = 0
        while len(nums):
            if sub in nums:
                i = nums.index(sub)
                nums = nums[i+1:]
                count += 1
            else:
                break

        print(count)
    except Exception as e:
        break
