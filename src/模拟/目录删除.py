n = 5  # 目录数
target = 8  # 需要删除的目录ID
dropnums = {target}  # 用于存放需要删除目录(target)的所有字目录集合
arr = [
    [8, 6],
    [10, 8],
    [6, 0],
    [20, 8],
    [2, 6]]  # 数据已经处理为int类型

# 用于循环添加需删除的子目录
while True:
    len1 = len(dropnums)
    for a, b in arr:
        if b in dropnums:
            dropnums.add(a)  # 添加子目录ID到集合中
    len2 = len(dropnums)
    if len1 == len2:  # 如果集合长度不变，表示target的所有子目录都已添加
        break

# 删除包含target子目录的所有记录（不包含target）
dropnums.discard(target)
dropidx = []
for i, (a, b) in enumerate(arr):
    if a in dropnums or b in dropnums:
        dropidx.append(i)
dropidx.sort(reverse=True)
for i in dropidx:
    del arr[i]
# 将剩余记录处理为ans集合
ans = set()
for a, b in arr:
    ans.add(a)
    ans.add(b)
# 集合删除target与根目录0
ans.discard(target)
ans.discard(0)
# 排序输出
print(" ".join(sorted(map(str, ans))))