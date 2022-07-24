while 1:
    try:
        m = int(input())

        if 1 >= m or m >= 100:
            print("ERROR!")
        else:
        	# 模拟1-100的圈
            nums = list(range(1, 101))
            i = 0
            while len(nums) >= m:
            	# 记录需要移除的数，也就是报的 m 的数
                cache = list(range(m - 1, len(nums), m))
                nums_ = []
                for i in range(len(nums)):
                	# 列表最后一个 m 后面的数，再下一轮 是列表的头
                	# 比如 [1,2,3,4,5] 报数到 3 ；
                	# 下一轮是 [4,5,1,2]
                    if i > cache[-1]:
                        nums = nums[i:] + nums_
                        break
                    elif i not in cache:
                        nums_.append(nums[i])
                else:
                    nums = nums_

            nums.sort()
            print(",".join(list(map(str, nums))))
    except Exception as e:
        break
