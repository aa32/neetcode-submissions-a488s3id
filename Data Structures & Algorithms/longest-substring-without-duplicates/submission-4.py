# abbbca
# l=0, r=0 , {a:0}
# l=0,r=1 , {a:0,b:1}
# r=2, {a:0,b:2} , l =r
# r =3 , {a:0,b:3} , l =3
# r =4 , {a:0,b:3,c:4}, l=3
# r=5 , {a:5,b:3,c:4} , l=5

# dvdfeggd:

# l=0,r=0 , {d:0} , len =1
# l=0,r=1 ,  {d:0,v:1}, len 2
# l=0,r-2 , l= 0+1 , {d:2,v:1} 
# l =1, r=3 , {d:2,v:1,f:3}, len 3


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len =0
        l=0
        hash_set = {}
        for r in range(len(s)):
            if s[r] in hash_set:
                l=max(l, hash_set[s[r]]+1)
      
            hash_set[s[r]]=r
            max_len = max(max_len,r-l+1)

        
        return max_len



        