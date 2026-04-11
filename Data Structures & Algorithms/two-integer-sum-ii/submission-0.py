class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lpoint=0
        rpoint=len(numbers)-1

        while(lpoint<rpoint):
            if numbers[lpoint]+numbers[rpoint]>target:
                rpoint-=1
            elif numbers[lpoint]+numbers[rpoint]<target:
                lpoint+=1

            else:
                return [lpoint+1,rpoint+1]     