import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_ = {}  # nums[i]:对应出现的次数
        for i in range(len(nums)):
            map_[nums[i]] = map_.get(nums[i], 0) + 1
        #print(map_)

        pri_que = []  # 小顶堆

        for key, freq in map_.items():
            heapq.heappush(pri_que, (freq, key))
            #print(pri_que,"-------")
            if len(pri_que) > k:  # 如果堆的大小大于了K，则队列弹出，保证堆的大小一直为k
                heapq.heappop(pri_que)
                #print(pri_que,".......")
        result = [0] * k
        for i in range(k - 1, -1, -1):
        #for i in range(k):
            result[i] = heapq.heappop(pri_que)[1]
        return result