# encoding = UTF-8
class Test(object):
    cookie ='' # 静态成员变量

    def __init__(self,cookies):  # 构造函数
        self.cookie = self.cookies  # 成员变量value1,此处的value1和静态的value1不是同一个变量
        #self.value2 = 200  # 成员变量value2

    def getValue(self):  # 类函数
        print(self.cookie)
        print(self.value2)

    def setValue(self):  # 类函数
        self.value1 = 1
        self.value2 = 2

    def classfun(self):  # 类方法
        print(Test.value1)
        print(self.value1)  # 可以使用参数cls来访问静态成员变量，也可以使用 "类名.静态成员变量"访问
        # print(cls.value2)   error  // 在类方法中和C++一样， 不能使用非静态成员变量

    @staticmethod
    def staticfun():  # 类静态方法
        print(Test.value1)
        # print(Test.value2) error  // 在类的静态成员函数中和C++一样， 不能使用非静态成员变量


if __name__ == "__main__":
    obj1 = Test()
    obj1.getValue()
    obj1.classfun()
    obj1.staticfun()
    print("-1")
    Test.value1 = 333
    print("-2")
   # Test.classfun()
    print("-3")
    Test.staticfun()
    print("-4")
    obj2 = Test()
    print("-5")
    obj2.setValue()
    print("-6")
    obj2.getValue()
    print("-7")
    obj1.getValue()
    Test.staticfun()