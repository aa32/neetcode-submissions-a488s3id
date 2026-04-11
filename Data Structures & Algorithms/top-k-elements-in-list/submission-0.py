import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = Counter(nums).items()
        print(type(nums_count))
        nums_count = sorted(nums_count ,key= lambda x : x[1],reverse=True)
        res_arr=[]
        for i in range (k):
            res_arr.append(nums_count[i][0])
        return res_arr
        
          
