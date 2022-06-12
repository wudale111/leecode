from typing import List
class Solution:
    def maopaosort(self,array:List)->List:
        for i in range(0,len(array)-1):
            for j in range(0,len(array)-1-i):
                if array[j]>array[j+1]:
                    c = array[j+1]
                    array[j+1] = array[j]
                    array[j] = c
        return array



A = Solution()
A.maopaosort([1,3,7,2,4,5])
print(A.maopaosort([1,3,7,2,4,5]))