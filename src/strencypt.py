'''
描述
对输入的字符串进行加解密，并输出。

加密方法为：

当内容是英文字母时则用该英文字母的后一个字母替换，同时字母变换大小写,如字母a时则替换为B；字母Z时则替换为a；

当内容是数字时则把该数字加1，如0替换1，1替换2，9替换0；

其他字符不做变化。

解密方法为加密的逆过程。
数据范围：输入的两个字符串长度满足 1 \le n \le 1000 \1≤n≤1000  ，保证输入的字符串都是只由大小写字母或者数字组成
输入描述：
第一行输入一串要加密的密码
第二行输入一串加过密的密码
'''
class Solution:
    def encypt(self,str1):
        str2 = []
        for i in str1:
            if i.islower():
                if i == 'z':
                    end = 'A'
                    str2.append(end)
                else:
                    start = ord(i)+1
                    end = chr(start).upper()
                    str2.append(end)
            if i.isupper():
                if i =='Z':
                    end = 'a'
                    str2.append(end)
                else:
                    start = ord(i)+1
                    end =chr(start).lower()
                    str2.append(end)
            if i.isnumeric():
                if int(i) == 9:
                    #此处要注意，将数字转化为字符串
                    end = '0'
                    str2.append(end)
                else:
                    end = str(int(i) + 1)
                    str2.append(end)
        str3 = ''
        for j in str2:
            str3 +=j
        return str3


    def decypt(self,str2):
        str3= []
        for i in str2:
            if i.islower():
                if i == 'a':
                    end = 'Z'
                    str3.append(end)
                else:
                    start = ord(i)-1
                    end = chr(start).upper()
                    str3.append(end)
            if i.isupper():
                if i =='A':
                    end = 'z'
                    str3.append(end)
                else:
                    start = ord(i)-1
                    end =chr(start).lower()
                    str3.append(end)
            if i.isnumeric():
                if int(i) == 0:
                    end = '9'
                    str3.append(end)
                else:
                    end = str(int(i)-1)
                    str3.append(end)
        str4 = ''
        for j in str3:
            str4 +=j
        return str4

A = Solution()
str1 = input()
str2 = input()
print(A.encypt(str1))
print(A.decypt(str2))


# def check(a, b):
#     L1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
#     L2 = "BCDEFGHIJKLMNOPQRSTUVWXYZAbcdefghijklmnopqrstuvwxyza1234567890"
#     result = ""
#     if b == 1:
#         for i in a:
#             result += L2[L1.index(i)]
#     elif b == -1:
#         for i in a:
#             result += L1[L2.index(i)]
#     return result
#
#
# while True:
#     try:
#         print(check(input(), 1))
#         print(check(input(), -1))
#
#     except:
#         break
