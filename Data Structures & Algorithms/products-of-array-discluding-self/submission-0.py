
# nums = [1,2,4,6]
# left_prod =[1,1,2,8]


# [6,4,2,1] = [1,6,24,48]

# right_prod = [48,24,6,1]


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lft_prd =[]
        rght_prd =[]

        prod_l =1
        prod_r =1
        rev_num = nums[::-1]

        res =[]

        for i in range(len(nums)):
            if i>0:
                prod_l = prod_l*nums[i-1]
                prod_r = prod_r*rev_num[i-1]
            lft_prd.append(prod_l)
            rght_prd.append(prod_r)

        
        rght_prd = rght_prd[::-1]



        for i in range(len(nums)):
            res.append(lft_prd[i]*rght_prd[i])

        return res






        
            
           
            

            
            



        