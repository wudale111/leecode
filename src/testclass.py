
class A(object):

    def __init__(self):#系统定义方法
        self.string='A string'
        self._string='A _string'
        self.__string='A __string'#私有变量

    def fun(self):
        return self.string + ' fun-A'

    def _fun(self):
        return self._string+'  _fun-A'

    def __fun(self):#私有方法
        return self.__string+' __fun-A'

    def for__fun(self):#内部调用私有方法
        return self.__fun()

class B(A):

    def __init__(self):#系统定义方法
        self.string = 'B string'

'''
a=A()
print (a.string)
print (a._string)
# print a.__string 不可访问

print (a.fun())
print( a._fun())
#print a.__fun() 不可访问
print(a.for__fun())


b=B()
print (b.fun())
print (b.fun().__len__())#系统定义函数
'''