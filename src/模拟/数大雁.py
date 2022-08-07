#leecode:1419
'''
思想就是维护croak的个数，如果遇到当前字母，则肯定是由前面字母过来，前面字母数-1。
如遇到r，则必是c->r，所以c--
k代表结尾，其实也是青蛙的起始（一次喊叫结束），所以遇到c的时候，先去消耗k，没有k了，需要新青蛙，答案+1

示例 1：

输入：croakOfFrogs = "croakcroak"
输出：1
解释：一只青蛙 “呱呱” 两次
示例 2：

输入：croakOfFrogs = "crcoakroak"
输出：2
解释：最少需要两只青蛙，“呱呱” 声用黑体标注
第一只青蛙 "crcoakroak"
第二只青蛙 "crcoakroak"


'''
# while 1:
#     try:
#         croakOfFrogs = input()
#         base = "quack"
#         states = [0] * len(base)
#         dp = []
#         for i in range(len(croakOfFrogs)):
#             index = base.index(croakOfFrogs[i])
#             if index == 0:
#                 states[index] += 1
#             else:
#                 if states[index - 1]:
#                     states[index - 1] -= 1
#                     states[index] += 1
#
#                 if base[-1] == croakOfFrogs[i]:
#                     if states[-1] != 0:
#                         # 计算剩余字符串是否满足剩余的叫声
#                         temp = [t for t in states]
#                         temp[-1] = 0
#                         max_ = sum(temp)
#                         for j in range(i, len(croakOfFrogs)):
#                             index = base.index(croakOfFrogs[j])
#                             if temp[index - 1]:
#                                 temp[index - 1] -= 1
#                                 temp[index] += 1
#                             if temp[-1] == max_:
#                                 break
#                         dp.append(temp[-1] + 1)
#                         states[-1] -= 1
#
#         print(max(dp) if dp else -1)
#     except Exception as e:
#         break


# public int minNumberOfFrogs(String croakOfFrogs) {
#         int c,r,o,a,k;
#         c = 0; r = 0; o = 0; a = 0;k = 0;
#         char []croakOfFrogs = croakOfFrogs.toCharArray();
#         int res = 0;
#         for(int i = 0;i < croakOfFrogs.length;i++){
#             if(croakOfFrogs[i] == 'c'){
#                 if(k > 0){k--;}else{res++;}
#                 c++;
#             }else if(croakOfFrogs[i] == 'r'){
#                 c--;r++;
#             }else if(croakOfFrogs[i] == 'o'){
#                 r--;o++;
#             }else if(croakOfFrogs[i] == 'a'){
#                 o--;a++;
#             }else if(croakOfFrogs[i] == 'k'){
#                 a--;k++;
#             }
#             if(c < 0 || r < 0 || o < 0 || a < 0){
#                 break;
#             }
#         }
#         if(c != 0 || r != 0 || o != 0 || a != 0){
#             return -1;
#         }
#         return res;
#     }

def minNumberOfFrogs(croakOfFrogs):
        #int c,r,o,a,k
        c = 0; r = 0; o = 0; a = 0;k = 0
        #char []croakOfFrogs = croakOfFrogs.toCharArray()
        res = 0
        for i in range(len(croakOfFrogs)):
            if croakOfFrogs[i] == 'c':
                if k > 0:
                    k -=1
                else:
                    res +=1
                c +=1
            elif croakOfFrogs[i] == 'r':
                c -=1
                r +=1
            elif croakOfFrogs[i] == 'o':
                r -=1
                o +=1
            elif croakOfFrogs[i] == 'a':
                o -=1
                a +=1
            elif croakOfFrogs[i] == 'k':
                a -=1
                k +=1

            if c < 0 or r < 0 or o < 0 or a < 0:
                break

        if c != 0 or r != 0 or o != 0 or a != 0:
            return -1

        return res
if __name__=='__main__':
    croakOfFrogs='crcoakroak'

    print(minNumberOfFrogs(croakOfFrogs))