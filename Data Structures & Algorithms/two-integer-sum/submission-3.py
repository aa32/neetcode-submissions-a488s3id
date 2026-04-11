
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checkDict = {}
        for i,num in enumerate(nums):
            complement = target-num
            if complement not in checkDict:
                checkDict[num]=i
            else:
                return [checkDict[complement],i]

        