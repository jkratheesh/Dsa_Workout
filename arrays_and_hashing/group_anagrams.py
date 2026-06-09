#time complexity with o(nklogk) and space complexity o(nk)
#could do better with o(nk) by tuple [0]*26

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for ch in strs:
            key = ''.join(sorted(ch))

            result[key].append(ch)

        return list(result.values())        