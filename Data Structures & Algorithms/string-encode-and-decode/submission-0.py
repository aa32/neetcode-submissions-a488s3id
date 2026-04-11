# # ["Hello","World!#"]
# # encoded s = "5#Hello7#World!#"
#                i
#                j

class Solution:
    def encode(self, strs: List[str]) -> str:
      res = ""
      for i in range(len(strs)):
        res +=  str(len(strs[i])) + '#' + strs[i]

      return res

    def decode(self, s: str) -> List[str]:
      res = []
      i = 0
      while (i<len(s)):
        j=i
        # print("i",i)
        while (s[j]!='#'):
          j+=1
        length = int(s[i:j])
        res.append(s[j+1:j+1+length])
        i = j+length+1
        # print(res)

      return res





      

