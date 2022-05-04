class Solution:
    def sentencereverse(self,str2):
        str = str2.split(" ")
        list = str[::-1]
        #print(list)
        for i in list:
            print(i,end=" ")


A = Solution()
str2 = input()
str3 = str2.replace(" ",'')
#对字符串去掉空格后，判断是否都是字母，且大小匹配要求。
if str3.isalpha() == True and len(str2) <= 1000:
    A.sentencereverse(str2)