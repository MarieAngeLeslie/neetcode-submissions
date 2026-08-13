class Solution:
    def isValid(self, s: str) -> bool:
        open_close_characters = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        stack = []
        for character in s :
            if character in open_close_characters :
                if stack and stack[-1] == open_close_characters[character] :
                    stack.pop()
                else:
                    return False
            else :
                stack.append(character)


        return False if stack else True