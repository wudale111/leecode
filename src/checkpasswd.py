# 构造一个检查函数 checkLegal
# 1）生成一个长度为3的所有子串序列（因为长度大于4的相同子串，必定存在长度3的相同子串)；
# 2）if len(set(sub)) < len(sub):return False python 用set去重，判断长度就可以知道是否有重复；
# 3）类型用正则匹配，如果匹配到目标数据格式 type_ += 1；
# 4）最后return True if type_ >= 3 else False；
# 5）处理多行输入输出，调用该函数即可。

# def checkLegal(pswd):
#     if len(pswd) <= 8:return False
#     else:
#         #最大重复子串长度2+
#         sub = []
#         for i in range(len(pswd)-2):
#             sub.append(pswd[i:i+3])
#         if len(set(sub)) < len(sub):return False
#         #check type
#         type_ = 0
#         import re
#         Upper = '[A-Z]'
#         Lowwer = '[a-z]'
#         num = '\d'
#         chars = '[^A-Za-z0-9_]'
#         patterns = [Upper, Lowwer, num, chars]
#         for pattern in patterns:
#             pw = re.search(pattern, pswd)
#             if pw : type_ += 1
#         return True if type_ >= 3 else False
# while True:
#     try:
#         pswd = input()
#         print('OK' if checkLegal(pswd) else 'NG')
#     except:
#         break

def check(pw):
    if len(pw) <= 8:  # 判断密码的长度
        return False

    checks = [0, 0, 0, 0]  # 四种情况满足三种的辅助列表
    for c in pw:
        if c.isupper():  # 大写字母
            checks[0] = 1
        elif c.islower():  # 小写字母
            checks[1] = 1
        elif c.isdigit():  # 数字
            checks[2] = 1
        else:  # 其他字符
            checks[3] = 1
    if sum(checks) < 3:
        return False

    dc = {}
    for i in range(len(pw) - 2):  # 遍历所有的子字符串起点
        if pw[i:i + 3] in dc:  # 在字典中搜索
            return False
        else:  # 如果未曾经出现过则加入字典中，等待之后的判定
            dc[pw[i:i + 3]] = 1

    return True


while True:
    try:
        pw = input()
        if check(pw):
            print('OK')
        else:
            print('NG')
    except:
        break

# def check(s):
#     if len(s) <= 8:
#         return 0
#     a, b, c, d = 0, 0, 0, 0
#     for item in s:
#         if ord('a') <= ord(item) <= ord('z'):
#             a = 1
#         elif ord('A') <= ord(item) <= ord('Z'):
#             b = 1
#         elif ord('0') <= ord(item) <= ord('9'):
#             c = 1
#         else:
#             d = 1
#     if a + b + c + d < 3:
#         return 0
    #遍历长度为3的子字符串，以这个子串进行切割，只有两段则没有相同长度为3的子串。
#     for i in range(len(s) - 2):
#         if len(s.split(s[i:i + 3])) >= 3:
#             return 0
#     return 1
      #遍历长度为3的子字符串，利用集合进行去重，判断是否有重复的子串
#       for i in range(len(s)-2):
#           x.append(s[i:i+3])
#       if len(set(x)) < len(x):
#           return 0
#       else:
#           return 1
#
#
# while 1:
#     try:
#         print('OK' if check(input()) else 'NG')
#     except:
#         break

