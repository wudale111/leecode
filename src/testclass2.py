class Test(object):
    cookie ='' # 静态成员变量

    def __init__(self,cookies):  # 构造函数
        self.cookie = cookies  # 成员变量value1,此处的value1和静态的value1不是同一个变量
        #self.value2 = 200  # 成员变量value2

    def getValue(self):  # 类函数
        print(self.cookie)
    def testb(self):
        print("b")

    def main(self):
        self.getValue()
        self.testb()

enumerate
A = Test('123')
A.main()