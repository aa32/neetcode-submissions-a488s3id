class Solution:
    def createDict(self,st):
        dict_st = {}
        for i in range(len(st)):
            ch = st[i]
            if ch in dict_st:
                dict_st[ch]+=1
            else:
                dict_st[ch]=1
        return dict_st

    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = self.createDict(s)
        dict_t = self.createDict(t)
        if dict_s==dict_t:
            return True
        else:
            return False

        