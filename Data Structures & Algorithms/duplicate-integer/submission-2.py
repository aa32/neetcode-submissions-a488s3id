class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)
        l_set = len(set_nums)
        l_list = len(nums)
        if l_set < l_list:
            return True
        else:
            return False
        