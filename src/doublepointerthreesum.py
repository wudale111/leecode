'''
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

来源：力扣（LeetCode）

你可以看下167,240,11这3题都可以用双指针，感受一下共同点。我是感觉，如果一组数据的结构，
能通过移动的方式来过滤以后的遍历，就可以使用双指针。如果不能使用，就去把数据组的构成可以
使用双指针的结构，比如有序数据，240中的有序矩阵；11题就直接从问题出发了，很巧妙
'''
# from typing import List
# import timeit
# start=timeit.default_timer()
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         path = []
#
#         def backtrack(nums,startindex):
#             if len(path)>3:
#                 return
#             if len(path) ==3 :
#                 if path[0]+path[1]+path[2]==0 :
#                     res.append(path[:])
#             for i in range(startindex, len(nums)):
#                 # if len(path) > 3:return
#                 # if i > startindex and nums[i] == nums[i - 1]: continue
#                 path.append(nums[i])
#                 backtrack(nums,i+1)
#                 path.pop()
#         backtrack(nums,0)
#         return res
#
# A = Solution()
# nums =[-1,0,1,2,-1,-4]
# A.threeSum(nums)
# print(A.threeSum(nums))
# end=timeit.default_timer()
# print('Running time: %s Seconds'%(end-start))


# import timeit
# start=timeit.default_timer()
# def threesum(nums):
#     res = []
#     for i in range(0, len(nums)):
#         for j in range(i+1, len(nums)):
#             for k in range(j+1, len(nums)):
#                 if nums[i] + nums[j] + nums[k]==0:
#                     res.append([nums[i],nums[j],nums[k]])
#     return res
# if __name__=='__main__':
#     nums = [-1,0,1,2,-1,-4]
#     print(threesum(nums))
# end=timeit.default_timer()
# print('Running time: %s Seconds'%(end-start))


# class Solution {
#     public List<List<Integer>> threeSum(int[] nums) {
#         Set result = new HashSet();
#         for(int i =0; i < nums.length; i++) {
#             for (int j = i +1; j< nums.length; j++) {
#                 for(int l = j +1; l < nums.length; l++) {
#                     if (nums[i] + nums[j]+nums[l] == 0) {
#                         List result2 = new ArrayList();
#                         result2.add(nums[i]);
#                         result2.add(nums[j]);
#                         result2.add(nums[l]);
#                          Collections.sort(result2);
#                         result.add(result2);
#                     }
#                 }
#             }
#         }
#         return new ArrayList<>(result);
#     }
# }



#双指针做法
import timeit
start=timeit.default_timer()
class Solution:
    def threeSum(self, nums):
        ans = []
        n = len(nums)
        nums.sort()
        for i in range(n):
            left = i + 1
            right = n - 1
            if nums[i] > 0:
                break
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left != right and nums[left] == nums[left + 1]: left += 1
                    while left != right and nums[right] == nums[right - 1]: right -= 1
                    left += 1
                    right -= 1
        return ans

nums = [-1, 0, 1, 2, -1, -4]
A =Solution()
print(A.threeSum(nums))
end=timeit.default_timer()
print('Running time: %s Seconds'%(end-start))
