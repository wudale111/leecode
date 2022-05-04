#python 输入输出，所有输入类型都是字符串类型,如果要输入整数，要使用int进行类型转换
n = int(input())
dic = {}
# idea: 动态建构字典
for i in range(n):
    line = input().split()
    key = int(line[0])
    value = int(line[1])
    dic[key] = dic.get(key, 0) + value  # 累积key所对应的value

for each in sorted(dic):  # 最后的键值对按照升值排序
    print(each, dic[each])