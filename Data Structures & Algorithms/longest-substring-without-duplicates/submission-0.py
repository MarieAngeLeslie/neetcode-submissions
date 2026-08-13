class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        if not string: return 0
        characters = ""
        characters_size = 0
        
        for main_pointer in range(len(string)):
            if string[main_pointer] not in characters:
                characters += string[main_pointer]
            else:
                characters_size = max(characters_size, len(characters))
                index = characters.find(string[main_pointer])
                characters = characters[index+1:] + string[main_pointer]
        
        return max(characters_size, len(characters))