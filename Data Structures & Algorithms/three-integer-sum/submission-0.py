class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num_srt = sorted(nums)
        res =[]
        for i in range(len(nums)):
            target = - (num_srt[i])
            l =i+1
            r = len(nums)-1
            
            if i>0 and num_srt[i]==num_srt[i-1]:
                continue

            while l<r:
                if num_srt[l]+num_srt[r]>target:
                    r-=1
                elif num_srt[l]+num_srt[r]<target:
                    l+=1
                else:
                    res.append([num_srt[i],num_srt[l],num_srt[r]])
                    l+=1
                    r-=1
                    while(l<r and num_srt[l]==num_srt[l-1]):
                        l+=1
                    while(l<r and num_srt[r]==num_srt[r+1]):
                        r-=1

        return res


                

        