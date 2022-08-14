while 1:
    try:
        m = int(input())
        for i in range(m):

            n = int(input())
            nums = [list(map(int, input().split())) for j in range(n)]
            nums = sorted(nums, key=lambda x: x[1], reverse=True)

            tal = 0
            bal = 0
            while nums:
                b, j = nums.pop(0)
                if bal >= b:
                    bal -= b
                else:
                    t = b - bal
                    tal += t

                if bal < j:
                    t = j - bal
                    bal += t
                    tal += t

            print(tal)
    except Exception as e:
        break
