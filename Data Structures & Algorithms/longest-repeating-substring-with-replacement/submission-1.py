#XXYZXWL  k =2
# Max_feq : {X:2,Y:1,Z:1} len =3  3-2<=k 
# i.e. len_str-max_frez<=k then max(max_len,len_str)
#As soon as len_str-max_frez<=k => you move left pointer to 1 step right.
# reduce the count of s[r] by 1 step.
# calculate max_freq.


# A. A  A  B A. B.  B --> 

# 1-0+1 =2 



class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt_ch ={}
        l=0
        res =0
        max_freq =0

        for r in range(len(s)):
            # print(r,s[r])
            cnt_ch[s[r]]= cnt_ch.get(s[r],0)+1
            max_freq = max(max_freq,cnt_ch[s[r]])

            while(r-l+1-max_freq > k):
                cnt_ch[s[l]]-=1
                l+=1
            # print(cnt_ch)
            # print("len",r-l+1)
            # print("max_freq",max_freq)
            # print(res)
            res = max(r-l+1,res)

        return res
        

        