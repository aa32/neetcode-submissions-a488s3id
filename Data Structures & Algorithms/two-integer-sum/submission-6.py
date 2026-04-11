# nums = [3,4,5,6], target = 7 O(n^2)
# {} -O(n) [element and indices] 
# hash map will have O(1) search

{3:0,}





class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)): #O(n)
            compl= target-nums[i]
            if compl in hashMap:
                return [hashMap[compl],i]
            else:
                hashMap[nums[i]]=i




        

        