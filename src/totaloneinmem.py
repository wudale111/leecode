# num = int(input())
# print(bin(num).count('1'))
x1 = int(input())
list = []
n = 0
while x1 >= 1:
    x2 = x1 % 2
    list.append(x2)
    x1 = x1 // 2

for word in list:
    if word == 1:
        n = n + 1

print(n)