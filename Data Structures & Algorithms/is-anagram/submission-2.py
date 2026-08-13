class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False

        for charater_of_s in s:
           for charater_of_t in t:
                if (charater_of_s == charater_of_t) :
                    new_string = t.replace(charater_of_t, "", 1)
                    t = new_string
                    break
                
        if len(t)==0 : 
            return True
        else :
            return False



# ça m'a pris 41min surtout du faite que je ne connaissais pas certaines syntaxe en python