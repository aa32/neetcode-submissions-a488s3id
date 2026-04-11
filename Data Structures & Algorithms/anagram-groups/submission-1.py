class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        
        for i in range(len(strs)):#O(n)
            word = strs[i]
            sorted_word = tuple(sorted(word)) #O(nlogn)
            if sorted_word in res:
                res[sorted_word].append(word)
            else:
                res[sorted_word]=[word]
        


        return list(res.values())