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
#islower()方法只要有小写就为true
# import re
# str = "abcA1"
# if str.isalpha() == True:
#     print("true")


# import re
#
# if not re.findall('[0-9]+',str):
#     raise SystemError("只能输入数字")

#sort与sorted，sort改变元序列且只能对列表排序。sorted不改变原列表，可以对列表和字典进行排序。默认是按ASCII码大小排序。
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

list= []
a,b,c,d =map(int,input().split())
list.append(a)
list.append(b)
list.append(c)
list.append(d)
print(list)
