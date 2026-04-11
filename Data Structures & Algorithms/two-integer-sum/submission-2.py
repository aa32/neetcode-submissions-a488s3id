# nums = [3,4,5,6], target = 9

# nums = [5,5]




class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            compl= target-nums[i]
            if compl not in hashMap:
                hashMap[nums[i]]=i
            else:
                return [hashMap[compl],i]

        retunr -1

