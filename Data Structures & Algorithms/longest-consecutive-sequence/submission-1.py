#O(nlogn)

nums = [2,20,4,10,3,4,5]
#[2,3,4,4,5,10,20]







class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums) # O(nlogn)
        print(sorted_nums)
        if len(nums)<1:
            return 0
    
        max_len =1
        length =1
        
        for i in range(len(nums)-1):
            if sorted_nums[i+1]==sorted_nums[i]+1:
                length +=1
                i+=1
            elif sorted_nums[i+1]==sorted_nums[i]:
                i+=1
            else:
                max_len = max(length,max_len)
                i+=1
                length =1

        max_len = max(length,max_len)
            
        return max_len
                

              
            





        





        
        