# nums = [2,20,4,10,3,4,5]
#  start -> 2
#  start =20
#  start 10.


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<1:
            return 0

        nums_set = set(nums)

        max_len =1
        for i in range(len(nums)):
            length =1
            if nums[i]-1 in nums_set:
                continue
            else:
                number = nums[i]
                while(number+1 in nums_set):
                    number = number+1
                    length+=1
                max_len = max(max_len , length)

        return max_len




        