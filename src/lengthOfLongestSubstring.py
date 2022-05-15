
#无重复字符的最长子串,双指针+滑动窗口

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         dic, res, i = {}, 0, -1   #i是左指针
#         for j in range(len(s)):  #j是右指针
#             if s[j] in dic:     #若当前元素在之前出现过，更新左指针
#                 #当之前出现的元素在左右指针中间，左指针更新为之前元素下标，若不在中间，左指针不变
#                 i = max(i, dic[s[j]])
#             dic[s[j]] = j    #将当前元素加入哈希表中
#             res = max(res, j - i)
#         return res

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         # Step 1: 定义需要维护的变量, 本题求最大长度，所以需要定义max_len, 该题又涉及去重，因此还需要一个哈希表
#         max_len, hashmap = 0, {}
#         # Step 2: 定义窗口的首尾端 (start, end)， 然后滑动窗口
#         start = 0
#         for end in range(len(s)):
#             # Step 3
#             # 更新需要维护的变量 (max_len, hashmap)
#             # i.e. 把窗口末端元素加入哈希表，使其频率加1，并且更新最大长度
#             hashmap[s[end]] = hashmap.get(s[end], 0) + 1
#             if len(hashmap) == end - start + 1:
#                 max_len = max(max_len, end - start + 1)
#             # Step 4:
#             # 根据题意,  题目的窗口长度可变: 这个时候一般涉及到窗口是否合法的问题
#             # 这时要用一个while去不断移动窗口左指针, 从而剔除非法元素直到窗口再次合法
#             # 当窗口长度大于哈希表长度时候 (说明存在重复元素)，窗口不合法
#             # 所以需要不断移动窗口左指针直到窗口再次合法, 同时提前更新需要维护的变量 (hashmap)
#             #字典为当前窗口的字符，和出现的次数
#             #如果字典有重复的元素，那么怎么找到它呢？
#             while end - start + 1 > len(hashmap):
#                 #head = 当前窗口开始的元素
#                 head = s[start]
#                 hashmap[head] -= 1
#                 #如果head为0代表着，窗口开始的元素
#                 if hashmap[head] == 0:
#                     #如果当前元素为-1为0，说明当前窗口开始元素不为重复元素在字典中删除当前窗口开始的元素。
#                     #不为重复元素为什么在字典中删除呢？因为下一个开始元素会在这之后，不删除会影响后面判断是否为子字符串
#                     del hashmap[head]
#                 #删除当前窗口开始元素后，当前开始窗口元素右移。如果当前窗口为重复元素了，末端元素继续后移
#                 start += 1
#         # Step 5: 返回答案 (最大长度)
#         return max_len
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         dic, res, i = {}, 0, 0   #i是左指针,字典存着Key:字符串，value:字符串索引，指针的定义代表什么含义
#         for j in range(len(s)):  #j是右指针
#             #print(dic,"循环开始")
#             if s[j] in dic:     #若当前元素在之前出现过，更新左指针
#                 #当之前出现的元素在左右指针中间，左指针更新为之前元素下标+1，若不在中间，左指针不变
#                 i = max(i, dic[s[j]]+1)
#                 #print(i,"左指针，有重复")
#             dic[s[j]] = j    #将当前元素加入哈希表中
#
#             res = max(res, j -i+1)
#             #print(res,"一次循环结束")
#         return res
# A = Solution()
# s="abcdcefghi"
# A.lengthOfLongestSubstring(s)
# print(A.lengthOfLongestSubstring(s))


#两种算法不同的关键是如何定义，有重复元素后，左指针的开始的值的定义。
#这道题要求返回的字符串长度，能做到返回最长子字符串的值？给定一个字符串找出只含一个字母的
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s.isalpha() or s.isdigit():
            return -1
        dic, res, left = {}, 0, 0   #i是左指针,字典存着Key:字符串，value:字符串索引，指针的定义代表什么含义
        for j in range(0,len(s)):  #j是右指针
            #print(dic,"循环开始")
            time = 0
            #print(s[left:j])
            for k in s[left:j+1] :
                if k.isalpha():
                    time +=1
            if time ==1:
                #print(left)
                res = max(res,j-left+1)
            else:
                left = max(left, j)
        return res
A = Solution()
s="aaaa11312"
A.lengthOfLongestSubstring(s)
print(A.lengthOfLongestSubstring(s))
