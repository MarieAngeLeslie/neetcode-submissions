class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        uniqueCharacters = set()
        left_pointer = 0
        result = 0

        for right_pointer in range(len(string)) :
            while string[right_pointer] in uniqueCharacters :
                uniqueCharacters.remove(string[left_pointer])
                left_pointer+=1
            uniqueCharacters.add(string[right_pointer])
            result = max(result, right_pointer - left_pointer + 1)
        
        return result