# class Parent:        # 定义父类
#    parentAttr = 100
#    a = 1
#    b = 2
#    #def __init__(self):
#    #   print "调用父类构造函数"
#    def a(self):
#        c = self.b
#        print(c)
# test = Parent()
# test.a()
# print(__name__)

# dic = {"1":2,"2":3,"3":4}
# print(dic["1"])
# if "2" in dic:
#     print("yes")
# import time
# # 获取当前时间
# current_time = int(time.time())
# print(current_time) # 1631186249
# # 转换为localtime
# localtime = time.localtime(current_time)
# # 利用strftime()函数重新格式化时间
# dt = time.strftime('%Y%m%d', localtime)
# print(dt) # 返回当前时间：2021:09:09 19:17:29
# str = "导入模板"+dt
# print(str)
# pri_que = [(1,2),(2,3)]
# print(len(pri_que))

#python 输入输出，所有输入类型都是字符串类型,如果要输入整数，要使用int进行类型转换
# for i in range(3):
#     a,b = input().split()
#     print(a,b)
# print(type(a))
#     #print("{0}={1}".format(a[0],a[1]))
#     #print(b)

# dic={1:2,5:3,4:5}
# print(sorted(dic))
# str = "1243"
# #list = [1,2,4,3]
# str.reverse()
# print(str)


# a = [1,2,3,4,5,6]
# print(a[-1])

#输入只能是字母, isalnum检测字符串是否只由字母和数字组成，不能有其他字符
# isalpha()方法检测字符串是否只由字母组成,不管大小写。
#islower()方法只能由小写字母组成
#isdigital,isnumeric()，是否只有数字组成，不能有其他字符
import re
# str = "AABBA"
# if str.isupper() == True:
#     print("true")


# import re
#
# if not re.findall('[0-9]+',str):
#     raise SystemError("只能输入数字")
#sorted对字符串排序后，将形成分隔开的字符串列表。
#sort与sorted，sort改变元序列且只能对列表排序,返回值为NONE。sorted不改变原列表，可以对列表和字典进行排序。默认是按ASCII码大小排序，ASCII码大写字母比小写字母小。数字<大写字目<小写字母
# list = ['a','f','g','B','a']
# #dic = {"a":1,"b":2,"d":4,"c":3}
# list.sort()
# print(list)

#print(list)
#print(sorted(list))
#
# str = "123"
# str.isnumeric()


#循环体中改变自增变量的值，不改变循环过程中，自增变量的值
#0 3 1 3 2
# for i in range(5):
#     print(i)
#     i = 3
#     print(i)


# 012 012 ,return之后，后面的for循环不会在继续。
# def test():
#     for i in range(5):
#         if i == 2:
#             return
#         for j in range(3):
#             print(j)
#             #j = j+1
# if __name__ == '__main__':
#     test()

# list= []
# a,b,c,d =map(int,input().split())
# list.append(a)
# list.append(b)
# list.append(c)
# list.append(d)
# print(list)

#set也可以用for i in set 来判断是否存在集合中
# a=set ()
# a.add("3")
# if '3' in a:
#  print('True')

# qw="I am Qiwsir you can read my articles im my blog".split()
# # print(sorted(chars,key=lambda x:len(x)))
# qw=['I', 'Am', 'Qiwsir', 'you', 'can', 'read', 'my', 'articles', 'im', 'my', 'blog']
# # 将原数组安装小写字母的顺序排序。排序出来的结果按原数组字符原样输出。如果有相同的大小写字母，按原来排序顺序输出。
# print(sorted(qw,key=str.upper) )       #依照字母升序排列


# str2=['1', 'p', 'b', 0, '1', 'b', 'Q', 'U', 'm', 'R', '4', 'h', '0', 'M', 'x', '7', '4', '5', '3', 'R', 'd', '3', 'O', 'l', 'n', 'K', 'W', '7', 'd']
# str4 = ''
# for j in str2:
#     str4 +=j
# print(str4)

# str1 = input()
# str2 = []
# for i in str1:
#     str2.append((ord(i)))
# str2.sort()
# print(str2)
# str3 =''
# for j in str2:
#     str3 +=chr(j)
# print(str3)


# num = 1.5
# str2 =str(num)
#
# str3 = str2.split('.')
# print(str3)
# if int(str3[1][0]) >=5:
#     print(int(str3[0])+1)
# else:
#     print(int(str3[0]))




# str1 ='I'
# print(ord(str1))
# num =73
# print(chr(num))

# print(' '.join('abcd'))
# res = []
# out_trains = ['3']
# in_trains = ['1','2']
# print(out_trains + in_trains[::-1])
# res.append(' '.join(out_trains + in_trains[::-1]))
# print(res)

# path =[]
# if 1>path[-1]:
#     print(path[-1])


#map不能用sort,是个内存值，能遍历，能用list
# n=map(int,input().split())
# print(n)
# for i in n:
#     print(i)
# n,k=map(int,input().split())
# str1=map(int,input().split())
# str1 =list(str1)
# print(str1)
# str1.sort() 
# for i in range(k+1):
#     print(n[i],end=(' '))

# dp=[0]*4
# dp[3]=max(6,7,8)
# print(dp[3])
# arr3=[1,1,2,6,4]
# print(list(set(arr3)))

# s='110011101'
# print(s.split('0'))


# print(2%3)
# print(2/3)
# print(2//3)
# 2
# 0.6666666666666666
# 0
dp=['12222', '12225', '12229', '12252', '12255', '12259']
ret = sorted(dp, key=lambda x: int(x))[0]
print(ret)