'''
题目描述
为了提升数据传输的效率，会对传输的报文进行压缩处理。
输入一个压缩后的报文，请返回它解压后的原始报文。
压缩规则：n[str]，表示方括号内部的 str 正好重复 n 次。
注意 n 为正整数（0 < n <= 100），str只包含小写英文字母，不考虑异常情况。
输入描述
输入压缩后的报文：

1）不考虑无效的输入，报文没有额外的空格，方括号总是符合格式要求的；
2）原始报文不包含数字，所有的数字只表示重复的次数 n ，例如不会出现像 5b 或 3[8] 的输入；

输出描述
解压后的原始报文

注：
1）原始报文长度不会超过1000，不考虑异常的情况

示例
输入
3[m2[c]]
1
输出
mccmccmcc
1
说明

m2[c] 解压缩后为 mcc，重复三次为 mccmccmcc

输入
10[k]2[mn3[j2[op]]]
1
输出
kkkkkkkkkkmnjopopjopopjopopmnjopopjopopjopop
1
思路分析
这道题是字符串处理的问题，同时字符串中嵌套括号，根据嵌套的括号进行报文解压缩，所以我们很容易想到用栈去解决问题。

首先把右括号之前的字符入栈。
遇到右括号时，开始进行解压缩，当栈不空的情况下开始出栈
出栈字符为字母时，暂存
出栈字符为数字时，判断如果前一个字符存在，是否仍为数字（处理两位数字，这里没有对数字100进行判断，如果需要再加一个判断即可）
循环num-1次累加暂存的字符串，因为本身有一次

注意：题目要求的压缩规则：n[str]，str只包含小写英文字母。所以左括号左边一定是数字。

3[[m2[c]]2[a]]
1
则不符合压缩规则。

'''

# import java.util.Scanner;
# import java.util.Stack;
#
# public class baoWenJieYaSuo {
#     public static void main(String[] args) {
#         Scanner in = new Scanner(System.in);
#         String str = in.nextLine();
#         Stack<Character> stack = new Stack<>();
#         String res = "";
#         char[] ch = str.toCharArray();
#         for (int i = 0; i < ch.length; i++) {
#             if (ch[i] == ']') {
#                 // 解压缩
#                 String tmpStr = "";
#                 while(!stack.isEmpty()) {
#                     char poll = stack.pop();
#                     if (poll >= 'a' && poll <= 'z') {  // 如果出栈的为字母
#                         tmpStr = String.valueOf(poll) + tmpStr;
#                     } else if (Character.isDigit(poll)) {  // 如果出栈的为数字
#                         int num = 0;
#                         if (!stack.isEmpty() && Character.isDigit(stack.peek())) {
#                             num = (stack.pop() - '0') * 10 + (poll - '0');
#                         } else {
#                             num = poll - '0';
#                         }
#                         String waitStr = tmpStr; // 需要将tempStr暂存起来
#                         for (int j = 0; j < num - 1; j++) { // 这里做 num -1 次的字符串相
#                             tmpStr += waitStr;
#                         }
#                     }
#                 }
#                 res += tmpStr;
#             }
#             stack.push(ch[i]);
#         }
#         System.out.println(res);
#     }
# }


def decompression(s):
    stack = []
    length = len(s)
    index = length - 1
    while index >= 0:
        if not s[index].isdigit():  # 非数字入栈
            stack.append(s[index])
            index -= 1
        else:  # 遇到数字时，解压
            num = ""
            res = ""
            while index >= 0 and s[index].isdigit():
                num = s[index] + num
                index -= 1
            # 说明此时的index处的字符一定时非数字的,此时栈顶一定是左括号
            while stack[-1] != "]":  # 获取栈中的字母
                tmp = stack.pop()
                if tmp != "[":  # 只要字母
                    res += tmp
            # 弹出栈顶的元素 # 右括号
            stack.pop()
            # 解压
            res = int(num) * res
            stack.append(res)
    stack.reverse()  # 反转字符串
    print("".join([item for item in stack if item not in "[]"]))


# s = "[m2[c2[oi2[jihyb]]]]"
s = "3[m2[c]]"
decompression(s)
