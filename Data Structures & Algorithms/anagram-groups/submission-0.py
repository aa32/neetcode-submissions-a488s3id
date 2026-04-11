# strs = ["act","pots","tops","cat","stop","hat"]
# strs_sort = ["act", "opst", "opst" ,"act","opst", "aht"]
# result = defaultdict(list)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            print(key)
            print(result)
            result[key].append(s)

        return list(result.values())

        