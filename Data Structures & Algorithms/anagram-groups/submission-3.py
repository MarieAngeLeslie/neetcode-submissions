class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for str in strs : 
            count = [0] * 26
            for character in str :
                count[ord(character) - ord('a')] += 1
            result[tuple(count)].append(str)
        return list(result.values())
