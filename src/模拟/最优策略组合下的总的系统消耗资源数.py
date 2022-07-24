'''
3
15 8 17
12 20 9
11 7 5
'''
while 1:
    try:
        n = int(input())
        nums = [list(map(int, input().split())) for _ in range(n)]

        def dfs(idx, com, val):
            # idx 用户id
            # com 三个策略
            # val 资源消耗
            if idx == n - 1:
                return val
            idx += 1
            #return min([dfs(idx, c, nums[idx][c]) + val for c in [0, 1, 2] if c != com])
            minlist=[]
            for c in [0,1,2]:
                if c !=com:
                    minlist.append(dfs(idx, c, nums[idx][c]) + val)
                    print(idx,c,nums[idx][c])
                    print(dfs(idx, c, nums[idx][c]),val,"-----------")
                    print(minlist,"1111111111")


            min2=min(minlist)
            return  min2

        dp = []
        for c in [0, 1, 2]:
            dp.append(dfs(0, c, nums[0][c]))

        print(min(dp))
    except Exception as e:
        break
