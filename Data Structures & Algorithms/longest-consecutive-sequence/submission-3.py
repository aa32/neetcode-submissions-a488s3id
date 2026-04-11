#O(nlogn)

# nums = [2,20,4,10,3,4,5]
# #[2,3,4,4,5,10,20]

# [2,3,4,5,        10,,,    20]

# [2] -> 3,4,5
# [10]-> x
# [20] x

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums) #O(1)
        if len(nums)<1:
            return 0
        max_len =1
        for i in range(len(nums)):
            length =1
            if nums[i]-1 not in nums_set:
                number = nums[i]
                while(number+1 in nums_set):
                    length+=1
                    number+=1


                max_len = max(length,max_len)

        return max_len


 




    
    
            





        





        
        