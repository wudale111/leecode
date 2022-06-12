# str1 = input()
# str2 = input()
# zichuang = ''
# for i in range(len(str1)):
#     if str1[i] in str2:
#         index2 = str2.index(str1[i])
#         print(index2,)
#         #怎么确认是连续的索引？
#         if index2 ==str2.index(str1[i]) +1:
#             zichuang.join(str1[i])
#         # else:
#         #     zichuang = str1[i]
# #print(zichuang)

# while True:
#     try:
#         s1=input()
#         s2=input()
#         if len(s1)>len(s2):#总体思路：从短的字符串中取子串，看其在长字符串中是否存在
#             s1,s2=s2,s1
#         length=0
#         for i in range(len(s1)):
#             for j in range(i+1,len(s1)):
#                 sub=s1[i:j]
#                 if sub in s2 and j-i>length:
#                     res=sub
#                     length=j-i
#         print(res)
#     except:
#         break


while True:
    try:
        a, b = input(), input() # a保存短，b保存长,总体思路：从短的字符串中取子串，看其在长字符串中是否存在
        if len(a) > len(b):
            a, b = b, a
        res = ''
        for i in range(0, len(a)):
            for j in range(i+1, len(a)):
                if a[i:j+1] in b and j+1-i > len(res):
                    res = a[i:j+1]
        print(res)
    except:
        break


