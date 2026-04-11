# nums = [1,2,2,3,3,3,3], k = 2

# {1:1, 2:2 ,3:4}
  
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_num = {}
        for i in range(len(nums)):
            if nums[i] in count_num:
                count_num[nums[i]]+=1
            else:
                count_num[nums[i]]=1
        
        count_num = list(count_num.items())
        print(count_num)

        sorted_count = sorted(count_num, key=lambda x: x[1], reverse=True)
        res = []
        for j in range(k):
            res.append(sorted_count[j][0])

        return res






