# # [-9,8,6,4]
# {-9:0, 8:1 ,6:2 , 4:3} 
# target =-3
# sorting - nlogn
# {-9,4,6,8} - n 
# n+nlogn
# ****************************
# n logn
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_set = {}

        for i in range(len(nums)):
            complement = target-nums[i]
            if complement not in nums_set:
                nums_set[nums[i]]=i
                # {3:0}
            else:
                return [nums_set[complement],i]





        