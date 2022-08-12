import java.util.*;
import java.util.regex.Pattern;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        //字符匹配：非法字符、类似“2aa”、类似“aaa”、以数字结尾的情况
        if (find(s,"[^0-9a-z]+") || find(s,"[0-9]([a-z])\\1") || find(s,"([a-z])\\1{2,}") || find(s,"[0-9]+$")){
            System.out.println("!error");
            return;
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (Character.isLetter(c))
                sb.append(c);
            else {
                int start = i;
                while (Character.isDigit(s.charAt(++i))) {}
                int n = Integer.parseInt(s.substring(start, i));
                if (n == 2) {//计数匹配
                    System.out.println("!error");
                    return;
                }
                for (int j = 0; j < n; j++)
                    sb.append(s.charAt(i));
            }
        }
        System.out.println(sb);
    }
    //正则部分匹配
    private static boolean find(String s, String regular) {
        return Pattern.compile(regular).matcher(s).find();
    }
}


  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    String line = in.nextLine();
    in.close();

    String res = decode(line);

    System.out.println(res);

  }

  private static String decode(String line) {
    String fixed = line.replaceAll("[a-z]|[0-9]", "");
    if (fixed.length() > 0) {
      return "!error";
    }

    StringBuilder res = new StringBuilder();
    char[] chars = line.toCharArray();
    int count = 1;
    for (int i = 0; i < chars.length; i++) {
      char cur = chars[i];

      if (Character.isLetter(cur)) {
        if (res.length() > 2
            && cur == res.charAt(res.length() - 1)
            && cur == res.charAt(res.length() - 2)) {
          return "!error";
        }
        if (count == 2) {
          return "!error";
        }
        for (int j = 0; j < count; j++) {
          res.append(cur);
        }
        count = 1;
      }
      int pos = i;
      while (Character.isDigit(chars[i])) {
        i++;
      }
      if (i > pos) {
        count = Integer.parseInt(line.substring(pos, i--));
      }
    }
    return res.toString();
  }
}