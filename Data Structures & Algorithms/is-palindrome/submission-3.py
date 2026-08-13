class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_pointer, right_pointer = 0, len(s)-1
        palindrome = True

        
        while(left_pointer < right_pointer) :

            if(s[left_pointer].isalnum() == False) : 
                left_pointer+=1
                continue

            if(s[right_pointer].isalnum() == False) : 
                right_pointer-=1
                continue

            if(s[left_pointer].lower() == s[right_pointer].lower()) : 
                left_pointer+=1
                right_pointer-=1
            else:
                palindrome = False
                return palindrome
        
        return palindrome