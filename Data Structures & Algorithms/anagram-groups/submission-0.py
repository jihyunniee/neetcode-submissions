class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for s in strs:
            x = "".join(sorted(s))
            if x in anagram_dict:
                anagram_dict[x].append(s)
            else:
                anagram_dict[x] = [s]
        
        result = []
        for l in anagram_dict.values():
            result.append(l)
        
        return result
        