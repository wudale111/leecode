'''

'''
# while 1:
#     try:
#         n = int(input())
#         nums = list(map(int, input().split()))
#         # 降序
#         nums.sort(reverse=True)
#
#         def dfs(total, sub):
#             for i in range(len(sub)):
#                 for j in range(len(sub)):
#                     if i != j:
#                         _t = sub[i] + sub[j] * 2
#                         if total == _t:
#                             return f"{total} {sub[i]} {sub[j]}"
#                         elif total < _t:
#                             break
#
#         for i in range(0, n-2):
#             r = dfs(nums[i], nums[i+1:][::-1])
#             if r:
#                 print(r)
#                 break
#         else:
#             print(0)
#     except Exception as e:
#         break


num = int(input())
nums = [int(x) for x in input().split()]
nums = sorted(nums)
res = '0'

for i in range(len(nums)-1, 0, -1):
    for j in range(0, i):
        for k in range(0, i):
            num1 = nums[i]
            num2 = nums[j]
            num3 = nums[k]
            if num1 == num2 + 2 * num3 and j != k:
                res = str(num1) + ' ' + str(num2) + ' ' + str(num3)
print(res)

# import java.io.BufferedReader;
# import java.io.IOException;
# import java.io.InputStreamReader;
# import java.util.Arrays;
# import java.util.Comparator;
#
# public
# class CheckNumCouple {
#
# public static void main(String[] args) throws NumberFormatException, IOException {
# BufferedReader br = new BufferedReader(new InputStreamReader(System.in ));
# String input;
#
#
# while ((input = br.readLine()) != null) {
# String[] numArrStr = input.split(" ");
# checkNumsCouple(numArrStr);
# }
# }
#
# / **
# *检查是否存在满足条件的数字组合
#  * @ param
# arrs
# 数组
# * /
# public
# static
# void
# checkNumsCouple(String[]
# arrs) {
# // 将字符数组转换为Integer数组
# Integer[]
# arr = new
# Integer[arrs.length];
# for (int i=0; i < arrs.length; i++) {
#     arr[i] = Integer.valueOf(arrs[i]);
# }
#
# // 让数组降序排列
# // 通过下面的循环，此处排序可以不要
# Arrays.sort(arr, new
# Comparator < Integer > ()
# {
#     public
# int
# compare(Integer
# o1, Integer
# o2) {
# return o2 - o1;
# }
# });
#
# // 定义标识，是否有满足条件数字组合
#         // 0
# 无；1
# 或其它值
# 有
# int
# index = 0;
#
# // 循环数组，让等式相等且3个元素的位置不相等
# for (int i=0; i < arr.length; i++) {
# for (int j=0; j < arr.length; j++) {
# for (int k=0; k < arr.length; k++) {
# if ((arr[i] == arr[j] + 2 * arr[k]) & & (i != j & & i != k & & j != k)) {
# index++;
# System.out.println(arr[i] + " " + arr[j] + " " + arr[k]);
# }
# }
# }
# }
#
# // 无满足条件的数字
# if (index == 0)
# {
#     System.out.println(0);
# }
# }
# }