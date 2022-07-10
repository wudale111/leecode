'''
 * 标题：求满足条件的最长子串的长度 | 时间限制：1秒 | 内存限制：262144K | 语言限制：不限
 * 给定一个字符串，只包含字母和数字，按要求找出字符串中的最长（连续）子串的长度，字符串本身是其最长的子串，子串要求：
 * 1、 只包含1个字母(a~z, A~Z)，其余必须是数字；
 * 2、 字母可以在子串中的任意位置；
 * 如果找不到满足要求的子串，如全是字母或全是数字，则返回-1。
 * 输入描述:
 * 字符串(只包含字母和数字)
 * 输出描述:
 * 子串的长度
 * 示例1
 * 输入
 * abC124ACb
 * 输出
 * 4
 * 说明 满足条件的最长子串是C124或者124A，长度都是4
 * 示例2
 * 输入
 * a5
 * 输出
 * 2
 * 说明 字符串自身就是满足条件的子串，长度为2
 * 示例3
 * 输入
 * aBB9
 * 输出
 * 2
 * 说明 满足条件的子串为B9，长度为2
 * 示例4
 * 输入
 * abcdef
 * 输出
 * -1
 * 说明 没有满足要求的子串，返回-1
'''

public class M_N_T_21 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String line = scanner.nextLine();

        char[] chars = line.toCharArray();

        ArrayList<Integer> integers = new ArrayList<>();
        integers.add(-1); // 关键点：第一个初始值，防止出现只有一个字母或者没有字母，无法进入循环的情况
        for (int i = 0; i < chars.length; i++) {
            char aChar = chars[i];
            if ((65 <= aChar && aChar <= 90) || (97 <= aChar && aChar <= 122)) {
                integers.add(i); // 存放所有字母出现的索引值
            }
        }
        integers.add(chars.length); // 关键点：第一个初始值，防止出现只有一个字母或者没有字母，无法进入循环的情况

        int len = -1;
        for (int i = 0; i < integers.size() - 2; i++) {
            int temp = integers.get(i + 2) - integers.get(i); // 每隔一个字母差值，即可判断可以放多少个数字
            if (temp > 2) {
                if (temp - 1 > len) {
                    len = temp - 1; // 出现更长的长度时才替换
                }
            }
        }

        System.out.println(len);
    }
}
