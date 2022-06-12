'''
描述
编写一个程序，将输入字符串中的字符按如下规则排序。
规则 1 ：英文字母从 A 到 Z 排列，不区分大小写。
如，输入： Type 输出： epTy
规则 2 ：同一个英文字母的大小写同时存在时，按照输入顺序排列。
如，输入： BabA 输出： aABb
规则 3 ：非英文字母的其它字符保持原来的位置。
如，输入： By?e 输出： Be?y
'''

str1 =input()
str2 = ''
for i in str1:
    if i.isalpha():
        str2 +=i
str2 = sorted(str2,key=str.lower)
str3 = ''
index = 0
for j in range(len(str1)):
    if str1[j].isalpha():
        str3 +=str2[index]
        index +=1
    else:
        str3 +=str1[j]
print(str3)




