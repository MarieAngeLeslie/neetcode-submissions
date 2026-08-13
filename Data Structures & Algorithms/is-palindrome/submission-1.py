class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lowercase = s.lower()
        left_pointer, right_pointer = 0, len(s_lowercase)-1
        palindrome = True

        
        while(left_pointer < right_pointer) :

            if(s_lowercase[left_pointer].isalnum() == False) : 
                left_pointer+=1
                continue

            if(s_lowercase[right_pointer].isalnum() == False) : 
                right_pointer-=1
                continue

            if(s_lowercase[left_pointer].lower() == s_lowercase[right_pointer].lower()) : 
                left_pointer+=1
                right_pointer-=1
            else:
                palindrome = False
                return palindrome
        
        return palindrome