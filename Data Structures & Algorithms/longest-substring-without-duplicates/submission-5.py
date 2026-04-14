#s = "zxyzxyz" 
#brute force -> O(n^2)
# l=0 
# hash_set = {}

# abbcdav
#  l=0 ,r=0 {a:0},
#  l=0, r=1 , (a:0,b:1) , max_le =2
#  l=0, r=2 , l=2 (a:0,b:2) , max_le =2
#  l=2,r=3 , (a:0,b:2,c:3) max_len =2
#  l=2,r=4 (a:0,b:2,c:3,d:4), max_len =3
#  l=2,r=5 (a:5,b:2,c:3,d:4), max_len =4
#  l=2,r=6 (a:5,b:2,c:3,d:4,v:6), max_len =5

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len =0
        l=0
        hash_set = {}
        for r in range(len(s)):
            if s[r] in hash_set:
                l = max(l,hash_set[s[r]]+1)
            hash_set[s[r]] =r
            max_len = max(r-l+1,max_len)
        return max_len

            

        