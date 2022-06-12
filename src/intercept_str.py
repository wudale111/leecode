while True:
    try:
        str1 = input()
        a = len(str1)
        #算出需要截取的次数，把末尾0补满。
        if a % 8 == 0:
            num =int(a/8)
        else:
            num = a // 8 + 1
        zero = '0' *(num*8-a)
        str1 = str1 + zero
        for k in range(0,num):
                print(str1[k*8:k*8+8])
    except:
        break

# while True:
#     try:
#         l = input()
#         for i in range(0, len(l), 8):
#             print("{0:0<8s}".format(l[i:i+8]))
#     except:
#         break