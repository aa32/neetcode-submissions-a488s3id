strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_lst = collections.defaultdict(list)

        for word in strs:
            sorted_wrd=sorted(word)
            ana_lst[tuple(sorted_wrd)].append(word)

        print(ana_lst.values())
        return list(ana_lst.values())
        