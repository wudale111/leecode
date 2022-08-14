bct = "aeiou"

while 1:
    try:
        k = int(input())
        nums = input()

        n = len(nums)
        nums = [1 if c in bct else 0 for c in nums]
        print(nums)
        max_ = 0
        i = 0
        j = min(k, n)
        while j < len(nums):
            count = nums[i:j].count(0)
            if count < k:
                j += 1
            elif count == k:
                max_ = max([j-i, max_])
                j += 1
            else:
                i += 1
        else:
            max_ = max([j - i, max_])

        print(max_)
    except Exception as e:
        break
