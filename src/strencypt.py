class Solution:
    def encypt(self,str):
        str2 = []
        for i in str:
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
                    end = 0
                    str2.append(end)
                else:
                    end = int(i)+1
                    str2.append(end)
        #for j in str2:
        print(''.join(str2))

    def decypt(self,str2):
        str2= []
        for i in str:
            if i.islower():
                if i == 'a':
                    end = 'Z'
                    str2.append(end)
                else:
                    start = ord(i)-1
                    end = chr(start).upper()
                    str2.append(end)
            if i.isupper():
                if i =='a':
                    end = 'Z'
                    str2.append(end)
                else:
                    start = ord(i)-1
                    end =chr(start).lower()
                    str2.append(end)
            if i.isnumeric():
                if int(i) == 0:
                    end = 9
                    str2.append(end)
                else:
                    end = int(i)-1
                    str2.append(end)
        #for j in str2:
        print(''.join(str2))
A = Solution()
str = input()
str2 = input()
A.encypt(str)
A.decypt(str2)




